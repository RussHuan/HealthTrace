# routes/exercise.py
# TODO 缺少卡路里计算
from flask import Blueprint, request, jsonify
from models import db
from models.exercise import Exercise
from models.user import User
from utils.response import success_response, error_response
from datetime import datetime, timedelta

exercise_bp = Blueprint('exercise', __name__, url_prefix='/exercise')

@exercise_bp.route('/records', methods=['POST'])
def add_exercise_record():
    """添加锻炼记录"""
    data = request.get_json()

    if not data:
        return error_response(400, "请求数据不能为空")
    
    # 验证必需字段
    required_fields = ['user_id', 'start_time', 'end_time', 'calories']
    for field in required_fields:
        if not data.get(field):
            return error_response(400, f"字段 {field} 不能为空")
        
    # 验证用户是否存在
    user = User.query.get(data['user_id'])
    if not user:
        return error_response(404, "用户不存在")
    
    try:
        # 解析时间
        start_time = datetime.fromisoformat(data['start_time'].replace('Z', '+00:00'))
        end_time = datetime.fromisoformat(data['end_time'].replace('Z', '+00:00'))

        # 创建记录
        exercise_record = Exercise(
            user_id=data['user_id'],
            start_time=start_time,
            end_time=end_time,
            calories=data['calories'],
            notes=data.get('notes', '')
        )       

        # 计算时长
        exercise_record.calculate_duration()

        db.session.add(exercise_record)
        db.session.commit()

        return success_response("运动记录添加成功", exercise_record.to_dict())
    
    except ValueError as e:
        return error_response(400, f"时间格式错误: {str(e)}")
    except Exception as e:
        db.session.rollback()
        return error_response(500, f"添加运动记录失败: {str(e)}")
    
@exercise_bp.route('/records/<int:user_id>', methods=['GET'])
def get_exercise_records(user_id):
    """获取用户的运动记录"""
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
        query = Exercise.query.filter_by(user_id=user_id)
        
        # 添加日期过滤
        if start_date:
            try:
                start_datetime = datetime.fromisoformat(start_date)
                query = query.filter(Exercise.start_time >= start_datetime)
            except ValueError:
                return error_response(400, "开始日期格式错误")
        
        if end_date:
            try:
                end_datetime = datetime.fromisoformat(end_date)
                query = query.filter(Exercise.start_time <= end_datetime)
            except ValueError:
                return error_response(400, "结束日期格式错误")
        
        # 按时间倒序排列并限制数量
        records = query.order_by(Exercise.start_time.desc()).limit(limit).all()
        
        # 转换为字典格式
        records_data = [record.to_dict() for record in records]
        
        return success_response("获取运动记录成功", records_data)
        
    except Exception as e:
        return error_response(500, f"获取运动记录失败: {str(e)}")
    
@exercise_bp.route('/records/<int:record_id>', methods=['PUT'])
def update_exercise_record(record_id):
    """更新运动记录"""
    data = request.get_json()
    
    if not data:
        return error_response(400, "请求数据不能为空")
    
    try:
        exercise_record = Exercise.query.get(record_id)
        if not exercise_record:
            return error_response(404, "运动记录不存在")
        
        # 更新字段
        if 'start_time' in data:
            exercise_record.start_time = datetime.fromisoformat(data['start_time'].replace('Z', '+00:00'))
        
        if 'wake_time' in data:
            exercise_record.end_time = datetime.fromisoformat(data['end_time'].replace('Z', '+00:00'))
        
        if 'notes' in data:
            exercise_record.notes = data['notes']
        
        # 重新计算运动时长
        exercise_record.calculate_duration()
        
        db.session.commit()
        
        return success_response("运动记录更新成功", exercise_record.to_dict())
        
    except ValueError as e:
        return error_response(400, f"时间格式错误: {str(e)}")
    except Exception as e:
        db.session.rollback()
        return error_response(500, f"更新运动记录失败: {str(e)}")
    
@exercise_bp.route('/records/<int:record_id>', methods=['DELETE'])
def delete_exercise_record(record_id):
    """删除运动记录"""
    try:
        exercise_record = Exercise.query.get(record_id)
        if not exercise_record:
            return error_response(404, "运动记录不存在")
        
        db.session.delete(exercise_record)
        db.session.commit()
        
        return success_response("运动记录删除成功")
        
    except Exception as e:
        db.session.rollback()
        return error_response(500, f"删除运动记录失败: {str(e)}")
    
@exercise_bp.route('/stats/<int:user_id>', methods=['GET'])
def get_exercise_stats(user_id):
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
        
        # 查询指定时间范围内的运动记录
        records = Exercise.query.filter(
            Exercise.user_id == user_id,
            Exercise.start_time >= start_date,
            Exercise.start_time <= end_date
        ).all()
        
        if not records:
            return success_response("暂无运动记录", {
                "total_records": 0,
                "average_duration": 0,
                "best_exercise": None,
                "worst_exercise": None
            })
        
        # 计算统计信息
        total_calories = sum(record.calories for record in records)
        total_duration = sum(record.duration_hours for record in records)
        average_duration = total_duration / len(records)       
        
        # 找出最佳和最差运动记录，
        best_exercise = max(records, key=lambda x: x.calories)
        worst_exercise = min(records, key=lambda x: x.calories)
        
        stats = {
            "total_records": len(records),
            "average_duration": round(average_duration, 2),
            "best_exercise": best_exercise.to_dict(),
            "worst_exercise": worst_exercise.to_dict(),
            "total_calories": round(total_calories, 2)
        }
        
        return success_response("获取运动统计成功", stats)
        
    except Exception as e:
        return error_response(500, f"获取运动统计失败: {str(e)}")