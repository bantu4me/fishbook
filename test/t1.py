class A:
    def exc_sql(self, sql):
        print(sql)

    def __enter__(self):
        print('connect')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('close')


def get_connect():
    return A()

with get_connect() as c:
    c.exc_sql('select * from system_user')

