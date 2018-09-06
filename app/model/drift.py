from sqlalchemy import Column, Integer, String, SmallInteger

from app.form.drift import DriftForm
from app.lib.enums import PendingStatus
from app.model.base import Base
from app.model.gift import Gift
from app.model.user import User


class Drift(Base):

    id = Column(Integer, primary_key=True)
    recipient_name = Column(String(20), nullable=False)
    address = Column(String(100), nullable=False)
    message = Column(String(200))
    mobile = Column(String(20), nullable=False)
    isbn = Column(String(13), nullable=False)
    book_title = Column(String(50))
    book_author = Column(String(30))
    book_img = Column(String(50))
    # 请求者信息
    requester_id = Column(Integer)
    requester_nickname = Column(String(20))
    # 礼物id
    gift_id = Column(Integer)
    # 赠送者信息
    gifter_id = Column(Integer)
    gifter_nickname = Column(String(20))
    # 鱼票状态
    _pending = Column('pending', SmallInteger, default=1)

    @property
    def pending(self):
        return PendingStatus(self._pending)

    @pending.setter
    def pending(self, status):
        self._pending = status.value

    def generate_drift(self, form:DriftForm, gift:Gift, user:User):
        self.recipient_name = form.recipient_name.data
        self.address = form.address.data
        self.message = form.message.data
        self.mobile = form.mobile.data
        self.isbn = gift.isbn
        self.book_title = gift.book.title
        self.book_author = gift.book.author
        self.book_img = gift.book.image
        self.requester_id = user.id
        self.requester_nickname = user.nickname
        self.gift_id = gift.id
        self.gifter_id = gift.user.id
        self.gifter_nickname = gift.user.nickname
        self.pending = PendingStatus(1)




