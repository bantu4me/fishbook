from contextlib import contextmanager

from flask_sqlalchemy import SQLAlchemy


class MySQLAlchemy(SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e


db = MySQLAlchemy()

from . import user
from . import book
