from contextlib import contextmanager

from flask_sqlalchemy import SQLAlchemy, BaseQuery


class MyQuery(BaseQuery):
    def filter_by(self, **kwargs):
        if 'status' not in kwargs.keys():
            kwargs['status'] = 1
        return super(MyQuery, self).filter_by(**kwargs)


class MySQLAlchemy(SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e


db = MySQLAlchemy(query_class=MyQuery)

from . import user
from . import book
