# routes/diet.py

from flask import Blueprint, request, jsonify
from models import db
from models.diet import Diet
from models.user import User
from utils.response import success_response, error_response
from datetime import datetime, timedelta

diet_bp = Blueprint('diet', __name__, url_prefix='/diet')

@diet_bp.route('/records', methods=['POST'])
def add_diet_record():
    """添加饮食记录"""
    data = request.get_json()

    if not data:
        return error_response(400, "请求数据不能为空")
    
    # 验证必需字段
    required_fields = ['user_id', 'meal_type', 'content', 'calories', 'date']
    for field in required_fields:
        if not data.get(field):
            return error_response(400, f"字段 {field} 不能为空")
        
    # 验证用户是否存在
    user = User.query.get(data['user_id'])
    if not user:
        return error_response(404, "用户不存在")
    
    try:
        # 解析日期 
        date = datetime.fromisoformat(data['date'].replace('Z', '+00:00')).date()

        # 创建记录
        diet_record = Diet(
            user_id=data['user_id'],
            meal_type=data['meal_type'],
            content=data['content'],
            calories=data['calories'],
            date=date
        )

        db.session.add(diet_record)
        db.session.commit()

        return success_response("饮食记录添加成功", diet_record.to_dict())
    
    except ValueError as e:
        return error_response(400, f"时间格式错误: {str(e)}")
    except Exception as e:
        db.session.rollback()
        return error_response(500, f"添加运动记录失败: {str(e)}")
    
@diet_bp.route('/records/<int:user_id>', methods=['GET'])
def get_diet_records(user_id):
    """获取用户的饮食记录"""
    # 验证用户
    user = User.query.get(user_id)
    if not user:
        return error_response(404, "用户不存在")
    
    try:
        # 获取查询参数
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')
        limit = request.args.get('limit', 30, type=int)
        
        # 构建查询
        query = Diet.query.filter_by(user_id=user_id)

    # 添加日期过滤
        if start_date:
            try:
                start_datetime = datetime.fromisoformat(start_date)
                query = query.filter(Diet.date >= start_datetime)
            except ValueError:
                return error_response(400, "开始日期格式错误")
        
        if end_date:
            try:
                end_datetime = datetime.fromisoformat(end_date)
                query = query.filter(Diet.date <= end_datetime)
            except ValueError:
                return error_response(400, "结束日期格式错误")
            
        # 按时间倒序排列并限制数量
        records = query.order_by(Diet.date.desc()).limit(limit).all()
        
        # 转换为字典格式
        records_data = [record.to_dict() for record in records]
        
        return success_response("获取饮食记录成功", records_data)
    
    except Exception as e:
        return error_response(500, f"获取饮食记录失败: {str(e)}")
    
@diet_bp.route('/records/<int:record_id>', methods=['PUT'])
def update_diet_record(record_id: int):
    """更新饮食记录"""
    data = request.get_json

    if not data:
        return error_response(400, "请求数据不能为空")
    
    try:
        diet_record = Diet.query.get(record_id)
        if not diet_record:
            return error_response(404, "记录不存在")
        
        # 更新字段
        if 'date' in data:
            diet_record.date = datetime.fromisoformat(data['date'].replace('Z', '+00:00'))

        if 'notes' in data:
            diet_record.notes = data['notes']

        db.session.commit()

        return success_response("记录更新成功", diet_record.to_dict())
    
    except ValueError as e:
        return error_response(400, f"时间格式错误: {str(e)}")
    except Exception as e:
        db.session.rollback()
        return error_response(500, f"更新记录失败: {str(e)}")
    
@diet_bp.route('/records/<int:record_id>', methods=['DELETE'])
def delete_diet_record(record_id):
    """删除饮食记录"""
    try:
        diet_record = Diet.query.get(record_id)
        if not diet_record:
             return error_response(404, "记录不存在")
        
        db.session.delete(diet_record)
        db.session.commit()

        return success_response("记录删除成功")
    
    except Exception as e:
        db.session.rollback()
        return error_response(500, f"删除记录失败: {str(e)}")
    
@diet_bp.route('/stats/<int:user_id>', methods=['GET'])
def get_diet_record(user_id):
    """获取用户饮食信息"""
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
        records = Diet.query.filter(
            Diet.user_id == user_id,
            Diet.date >= start_date,
            Diet.date <= end_date
        ).all()

        if not records:
            return success_response("暂无记录", {
                "total_records": 0,
                "total_calories": 0,
                "average_calories": 0
            })
        
        # 计算统计信息
        total_calories = sum(record.calories for record in records)

        stats = {
            "total_records": len(records),
            "total_calories": total_calories,
            "average_calories": round(total_calories / len(records), 2)
        }

        return success_response("获取统计数据成功", stats)
    
    except Exception as e:
        return error_response(500, f"获取运动统计失败: {str(e)}")