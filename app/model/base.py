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
