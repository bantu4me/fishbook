from flask import Flask

from flask_login import LoginManager
login = LoginManager()
from flask_mail import Mail
mail = Mail()
from app.model import db


def create_app():
    """
    :rtype: Flask
    """
    app = Flask(__name__)
    # 读取配置文件
    app.config.from_object('app.secure')
    # 注册蓝图
    register_blueprint(app)
    # 初始化dao
    db.init_app(app)
    db.create_all(app=app)
    # 初始化flask_login插件
    login.init_app(app)
    login.login_message = '请先注册或登录'
    login.login_view = 'web.login'
    # 初始化mail
    mail.init_app(app)
    return app


def register_blueprint(app: Flask):
    from app.web.blueprint import web
    app.register_blueprint(web)
