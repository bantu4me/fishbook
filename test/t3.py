import time
from threading import Thread

from werkzeug.local import Local

obj = Local()
obj.num = 1


def process_def():
    obj.num = 2
    print('in process_def obj.num=', obj.num)


t = Thread(target=process_def)
t.start()
time.sleep(1)

print('in main thread obj.num=', obj.num)
