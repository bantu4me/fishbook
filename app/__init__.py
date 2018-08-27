from flask import Flask


def create_app():
    app = Flask(__name__)
    # 注册蓝图
    register_blueprint(app)
    return app


def register_blueprint(app: Flask):
    from app.web.blueprint import web
    app.register_blueprint(web)
