# routes/auth.py

from flask import Blueprint, request, jsonify
from models.user import db, User
from utils.response import success_response, error_response

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

    db.session.delete(user)
    db.session.commit()

    return success_response("账号注销成功")
