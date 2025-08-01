# routes/sleep.py

from flask import Blueprint, request, jsonify
from models import db
from models.sleep import Sleep
from models.user import User
from utils.response import success_response, error_response
from datetime import datetime, timedelta

sleep_bp = Blueprint('sleep', __name__, url_prefix='/sleep')

@sleep_bp.route('/records', methods=['POST'])
def add_sleep_record():
    """添加睡眠记录"""
    data = request.get_json()
    
    if not data:
        return error_response(400, "请求数据不能为空")
    
    # 验证必需字段
    required_fields = ['user_id', 'sleep_time', 'wake_time']
    for field in required_fields:
        if not data.get(field):
            return error_response(400, f"字段 {field} 不能为空")
    
    # 验证用户是否存在
    user = User.query.get(data['user_id'])
    if not user:
        return error_response(404, "用户不存在")
    
    try:
        # 解析时间字符串
        sleep_time = datetime.fromisoformat(data['sleep_time'].replace('Z', '+00:00'))
        wake_time = datetime.fromisoformat(data['wake_time'].replace('Z', '+00:00'))
        
        # 创建睡眠记录
        sleep_record = Sleep(
            user_id=data['user_id'],
            sleep_time=sleep_time,
            wake_time=wake_time,
            quality_rating=data.get('quality_rating'),
            notes=data.get('notes', '')
        )
        
        # 计算睡眠时长
        sleep_record.calculate_duration()
        
        db.session.add(sleep_record)
        db.session.commit()
        
        return success_response("睡眠记录添加成功", sleep_record.to_dict())
        
    except ValueError as e:
        return error_response(400, f"时间格式错误: {str(e)}")
    except Exception as e:
        db.session.rollback()
        return error_response(500, f"添加睡眠记录失败: {str(e)}")

@sleep_bp.route('/records/<int:user_id>', methods=['GET'])
def get_sleep_records(user_id):
    """获取用户的睡眠记录"""
    # 验证用户是否存在
    user = User.query.get(user_id)
    if not user:
        return error_response(404, "用户不存在")
    
    try:
        # 获取查询参数
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')
        limit = request.args.get('limit', 30, type=int)
        
        # 构建查询
        query = Sleep.query.filter_by(user_id=user_id)
        
        # 添加日期过滤
        if start_date:
            try:
                start_datetime = datetime.fromisoformat(start_date)
                query = query.filter(Sleep.sleep_time >= start_datetime)
            except ValueError:
                return error_response(400, "开始日期格式错误")
        
        if end_date:
            try:
                end_datetime = datetime.fromisoformat(end_date)
                query = query.filter(Sleep.sleep_time <= end_datetime)
            except ValueError:
                return error_response(400, "结束日期格式错误")
        
        # 按时间倒序排列并限制数量
        records = query.order_by(Sleep.sleep_time.desc()).limit(limit).all()
        
        # 转换为字典格式
        records_data = [record.to_dict() for record in records]
        
        return success_response("获取睡眠记录成功", records_data)
        
    except Exception as e:
        return error_response(500, f"获取睡眠记录失败: {str(e)}")

@sleep_bp.route('/records/<int:record_id>', methods=['PUT'])
def update_sleep_record(record_id):
    """更新睡眠记录"""
    data = request.get_json()
    
    if not data:
        return error_response(400, "请求数据不能为空")
    
    try:
        sleep_record = Sleep.query.get(record_id)
        if not sleep_record:
            return error_response(404, "睡眠记录不存在")
        
        # 更新字段
        if 'sleep_time' in data:
            sleep_record.sleep_time = datetime.fromisoformat(data['sleep_time'].replace('Z', '+00:00'))
        
        if 'wake_time' in data:
            sleep_record.wake_time = datetime.fromisoformat(data['wake_time'].replace('Z', '+00:00'))
        
        if 'quality_rating' in data:
            sleep_record.quality_rating = data['quality_rating']
        
        if 'notes' in data:
            sleep_record.notes = data['notes']
        
        # 重新计算睡眠时长
        sleep_record.calculate_duration()
        
        db.session.commit()
        
        return success_response("睡眠记录更新成功", sleep_record.to_dict())
        
    except ValueError as e:
        return error_response(400, f"时间格式错误: {str(e)}")
    except Exception as e:
        db.session.rollback()
        return error_response(500, f"更新睡眠记录失败: {str(e)}")

@sleep_bp.route('/records/<int:record_id>', methods=['DELETE'])
def delete_sleep_record(record_id):
    """删除睡眠记录"""
    try:
        sleep_record = Sleep.query.get(record_id)
        if not sleep_record:
            return error_response(404, "睡眠记录不存在")
        
        db.session.delete(sleep_record)
        db.session.commit()
        
        return success_response("睡眠记录删除成功")
        
    except Exception as e:
        db.session.rollback()
        return error_response(500, f"删除睡眠记录失败: {str(e)}")

@sleep_bp.route('/stats/<int:user_id>', methods=['GET'])
def get_sleep_stats(user_id):
    """获取用户睡眠统计信息"""
    # 验证用户是否存在
    user = User.query.get(user_id)
    if not user:
        return error_response(404, "用户不存在")
    
    try:
        # 获取查询参数
        days = request.args.get('days', 7, type=int)
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        
        # 查询指定时间范围内的睡眠记录
        records = Sleep.query.filter(
            Sleep.user_id == user_id,
            Sleep.sleep_time >= start_date,
            Sleep.sleep_time <= end_date
        ).all()
        
        if not records:
            return success_response("暂无睡眠记录", {
                "total_records": 0,
                "average_duration": 0,
                "average_quality": 0,
                "best_sleep": None,
                "worst_sleep": None
            })
        
        # 计算统计信息
        total_duration = sum(record.duration_hours for record in records)
        average_duration = total_duration / len(records)
        
        quality_ratings = [record.quality_rating for record in records if record.quality_rating]
        average_quality = sum(quality_ratings) / len(quality_ratings) if quality_ratings else 0
        
        # 找出最佳和最差睡眠记录
        best_sleep = max(records, key=lambda x: x.duration_hours)
        worst_sleep = min(records, key=lambda x: x.duration_hours)
        
        stats = {
            "total_records": len(records),
            "average_duration": round(average_duration, 2),
            "average_quality": round(average_quality, 1),
            "best_sleep": best_sleep.to_dict(),
            "worst_sleep": worst_sleep.to_dict()
        }
        
        return success_response("获取睡眠统计成功", stats)
        
    except Exception as e:
        return error_response(500, f"获取睡眠统计失败: {str(e)}")
