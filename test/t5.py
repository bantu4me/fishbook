from contextlib import contextmanager


class A:
    def __enter__(self):
        print('get connection')
        return self

    def query(self):
        print('query...')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('close connection')


with A() as a:
    a.query()


class B:
    def query(self):
        print('query...')


@contextmanager
def create_query():
    print('get connection')
    yield B()
    print('close connection')


with create_query() as b:
    b.query()
