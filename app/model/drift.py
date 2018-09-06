from sqlalchemy import Column, Integer, String, SmallInteger

from app.lib.enums import PendingStatus
from app.model.base import Base


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
