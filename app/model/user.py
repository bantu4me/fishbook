import math

from flask import current_app
from flask_login import UserMixin
from sqlalchemy import Column, String, Integer, Boolean, Float

from app import login
from app.lib.utils import is_isbn_or_key
from app.lib.yushu_book import YushuBook
from app.model.base import Base
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


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
    def summary(self):
        return dict(
            nickname=self.nickname,
            beans=self.beans,
            email=self.email,
            send_receive=str(self.send_counter) + '/' + str(self.receive_counter)
        )

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, pwd):
        self._password = generate_password_hash(pwd)

    def check_pwd(self, raw):
        return check_password_hash(self._password, raw)

    def can_save_gift_or_wish(self, isbn) -> bool:
        '''
        通过传入isbn判断当前isbn对应书籍能否保存到心愿或礼物
        :param isbn:
        :return:
        '''
        isbn_or_key = is_isbn_or_key(isbn)
        if isbn_or_key == 'key':
            return False
        # isbn查询不到对应书籍，返回false
        yushubook = YushuBook()
        yushubook.search_by_isbn(isbn)
        if not yushubook.only:
            return False
        # 判断该isbn号是否已经存在用户的心愿或礼物列表中
        gift = Gift.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()
        wish = Wish.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()
        return True if not gift and not wish else False

    def generate_token(self):
        info = {'id': self.id, 'email': self.email}
        s = Serializer(secret_key=current_app.config['SECRET_KEY'], expires_in=60)
        return s.dumps(info).decode('utf-8')

    def can_send_drift(self):
        if self.beans < 1:
            return False
        if self.receive_counter == 0:
            return True if self.send_counter - self.receive_counter <= 2 else False
        elif self.receive_counter != 0:
            return True if math.ceil(self.send_counter / self.receive_counter) > 2 else False


@login.user_loader
def get_user(uid):
    return User.query.get(int(uid))


from app.model.gift import Gift
from app.model.wish import Wish
