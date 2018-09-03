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


def parse_isbn_count(isbn_count_list):
    isbn_count_dict = {}
    for i in isbn_count_list:
        isbn_count_dict[i[0]] = i[1]
    return isbn_count_dict


class MyTradesView:
    def __init__(self, goods, isbn_count_list):
        self.trades = []
        isbn_count_dict = parse_isbn_count(isbn_count_list)
        self.__parse(goods, isbn_count_dict)

    def __parse(self, goods, isbn_count_dict):
        self.trades = [self.__parse_single(good,isbn_count_dict) for good in goods]

    def __parse_single(self, good, isbn_count_dict):
        wishes_count = isbn_count_dict.get(good.isbn) if isbn_count_dict.get(good.isbn) else 0
        trade = {
            'id': good.id,
            'isbn': good.isbn,
            'image': good.book.image,
            'title': good.book.title,
            'author': good.book.author,
            'publisher': good.book.publisher,
            'price': good.book.price,
            'wishes_count': wishes_count
        }
        return trade