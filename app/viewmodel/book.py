from app.lib.yushu_book import YushuBook


def fix_price(price: str):
    if price:
        price = '￥' + price
        if price.endswith('元'):
            return price
        else:
            return price + '元'
    return '暂无售价信息'


class BookView:
    def __init__(self, book):
        self.title = book['title']
        self.publisher = book['publisher']
        self.price = fix_price(book['price'])
        self.pages = book['pages'] or ''
        self.summary = book['summary'] or ''
        self.image = book['image']
        self.author = ','.join(book['author'])
        self.isbn = book['isbn']
        self.pubdate = book['pubdate']
        self.binding = book['binding']
        fix_price('')

    @property
    def intro(self):
        return '/ '.join(filter(lambda x: True if x else False, [self.author, self.publisher, self.price]))


class BookPage:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill_book_page(self, yushubook: YushuBook):
        self.total = yushubook.total
        self.books = [BookView(book) for book in yushubook.books]
        self.keyword = yushubook.keyword

