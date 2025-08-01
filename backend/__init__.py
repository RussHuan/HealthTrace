import os

from flask import Flask

from models import db
from models import user
from routes.auth import auth_bp


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    
    # 数据库配置（使用 SQLite 示例）
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///health.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # 初始化 SQLAlchemy
    db.init_app(app)

    # 注册蓝图
    app.register_blueprint(auth_bp)

    # 创建数据库表
    with app.app_context():
        db.create_all()

    # a simple page that says hello
    @app.route('/')
    def hello():
        return 'Hello, World!'

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)