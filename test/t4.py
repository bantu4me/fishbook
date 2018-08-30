import time
from threading import Thread

from werkzeug.local import LocalStack

s = LocalStack()
s.push(1)


def process():
    print('top in proceess:', s.top)


t = Thread(target=process)

t.start()
time.sleep(1)

print('top in main:', s.top)


