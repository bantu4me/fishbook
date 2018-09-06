from enum import Enum


class PendingStatus(Enum):
    wait = 1
    success = 2
    reject = 3
    redraw = 4

    @classmethod
    def status_str(cls, you_are, status):
        status_map = {
            cls.wait: {
                'requester': '等待对方邮寄',
                'gifter': '等待你邮寄'
            },
            cls.reject: {
                'requester': '对方已拒绝',
                'gifter': '你已拒绝'
            },
            cls.redraw: {
                'requester': '你已撤销',
                'gifter': '对方已撤销'
            },
            cls.success: {
                'requester': '对方已邮寄',
                'gifter': '你已邮寄，交易完成'
            }
        }
        return status_map[status][you_are]


if __name__ == '__main__':
    print(PendingStatus(1))
    print(PendingStatus.status_str('requester', PendingStatus(1)))
