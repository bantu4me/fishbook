class TradesView:
    def __init__(self, goods):
        self.total = 0
        self.trades = []
        self.__parse(goods)

    def __parse(self, goods):
        self.total = len(goods)
        self.trades = [self.__parse_single(good) for good in goods]

    def __parse_single(self, good):
        time = good.create_datetime.strftime('%Y-%M-%d') if good.create_datetime else '未知'
        return {
            'id': good.id,
            'time': time,
            'user_name': good.user.nickname
        }
