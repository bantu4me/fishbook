from sqlalchemy import Column, Float, SmallInteger
from datetime import datetime

from app.model import db


class Base(db.Model):
    __abstract__ = True
    status = Column(SmallInteger, default=1)
    create_time = Column(Float)

    def __init__(self):
        self.create_time = datetime.now().timestamp()

    # 通用删除标记
    def delete(self):
        self.status = 0

    def set_attr(self, args_dic: dict):
        for k, v in args_dic.items():
            if k != 'id' and hasattr(self, k):
                setattr(self, k, v)

    @property
    def create_datetime(self):
        return datetime.fromtimestamp(self.create_time)
