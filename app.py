from flask import Flask
from app.web.blueprint import web

app = Flask(__name__)
app.register_blueprint(web)


if __name__ == '__main__':
    app.run()
