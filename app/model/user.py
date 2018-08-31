from flask_login import UserMixin
from sqlalchemy import Column, String, Integer, Boolean, Float

from app import login
from app.model.base import Base
from werkzeug.security import generate_password_hash, check_password_hash


class User(Base, UserMixin):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    nickname = Column(String(length=24), nullable=False)
    phone_number = Column(String(length=18), unique=True)
    email = Column(String(length=50), unique=True)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=2)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    wx_open_id = Column(String(length=50))
    wx_name = Column(String(length=32))
    _password = Column('password', String(256), nullable=False)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, pwd):
        self._password = generate_password_hash(pwd)

    def check_pwd(self, raw):
        return check_password_hash(self._password, raw)


@login.user_loader
def get_user(uid):
    print('in get user')
    return User.query.get(int(uid))
