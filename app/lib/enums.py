from enum import Enum


class PendingStatus(Enum):
    wait = 1
    success = 2
    reject = 3
    redraw = 4




if __name__ == '__main__':
    print(PendingStatus(1).name + ':' + str(PendingStatus(1).value))
