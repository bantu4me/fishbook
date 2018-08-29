from datetime import datetime
import time


class Base:
    t = datetime.now().timestamp()

    def __init__(self):
        t = datetime.now().timestamp()


a = Base()
print('time a:', a.t)

time.sleep(1)

b = Base()
print('time b:', b.t)
