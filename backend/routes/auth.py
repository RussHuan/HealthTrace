# routes/auth.py

from flask import Blueprint, request, jsonify, send_file
from models.user import db, User
from utils.response import success_response, error_response
import io
import json

auth_bp = Blueprint('auth', __name__, url_prefix='/users')

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    if not data or not data.get('username') or not data.get('password'):
        return error_response(400, "用户名或密码不能为空")

    if User.query.filter_by(username=data['username']).first():
        return error_response(409, "用户名已存在")

    user = User(username=data['username'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()

    return success_response("注册成功")


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if not data or not data.get('username') or not data.get('password'):
        return error_response(400, "用户名或密码不能为空")

    user = User.query.filter_by(username=data['username']).first()

    if user and user.check_password(data['password']):
        # 简化版：直接返回 userId，生产环境请改为 JWT 令牌
        return success_response("登录成功", user.id)
    else:
        return error_response(401, "用户名或密码错误")

@auth_bp.route('/change-password', methods=['PUT'])
def change_password():
    data = request.get_json()

    if not data or not data.get('username') or not data.get('old_password') or not data.get('new_password'):
        return error_response(400, "用户名、旧密码或新密码不能为空")

    user = User.query.filter_by(username=data['username']).first()

    if not user or not user.check_password(data['old_password']):
        return error_response(401, "用户名或旧密码错误")

    user.set_password(data['new_password'])
    db.session.commit()

    return success_response("密码修改成功")

@auth_bp.route('/delete-account', methods=['DELETE'])
def delete_account():
    data = request.get_json()

    if not data or not data.get('username') or not data.get('password'):
        return error_response(400, "用户名或密码不能为空")

    user = User.query.filter_by(username=data['username']).first()

    if not user or not user.check_password(data['password']):
        return error_response(401, "用户名或密码错误")

    # 在删除用户之前，可能需要删除所有关联的数据
    # 例如：
    # from models.diet import DietRecord
    # from models.exercise import ExerciseRecord
    # from models.sleep import SleepRecord
    # DietRecord.query.filter_by(user_id=user.id).delete()
    # ExerciseRecord.query.filter_by(user_id=user.id).delete()
    # SleepRecord.query.filter_by(user_id=user.id).delete()

    db.session.delete(user)
    db.session.commit()

    return success_response("账号注销成功")

@auth_bp.route('/export-data', methods=['GET'])
def export_data():
    # 在生产环境中，用户ID应从JWT令牌或会话中获取，而不是直接作为查询参数
    user_id = request.args.get('userId')
    if not user_id:
        return error_response(400, "用户ID不能为空")

    user = User.query.get(user_id)
    if not user:
        return error_response(404, "用户不存在")

    # 获取用户基本信息
    user_data = user.to_dict()

    # 在这里，你需要查询并收集所有与该用户相关的健康数据
    # 假设你还有 DietRecord, ExerciseRecord, SleepRecord 等模型
    # from models.diet import DietRecord
    # from models.exercise import ExerciseRecord
    # from models.sleep import SleepRecord

    # diet_records = [record.to_dict() for record in DietRecord.query.filter_by(user_id=user_id).all()]
    # exercise_records = [record.to_dict() for record in ExerciseRecord.query.filter_by(user_id=user_id).all()]
    # sleep_records = [record.to_dict() for record in SleepRecord.query.filter_by(user_id=user_id).all()]

    exported_data = {
        "user_info": user_data,
        # "diet_records": diet_records,
        # "exercise_records": exercise_records,
        # "sleep_records": sleep_records,
        "message": "这是用户数据导出示例。在实际应用中，这里会包含所有关联的健康记录。"
    }

    # 返回JSON数据
    return success_response("数据导出成功", exported_data)

