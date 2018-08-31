from app.lib.yushu_book import YushuBook


class BookView:
    def __init__(self, book):
        self.title = book['title']
        self.publisher = book['publisher']
        self.price = book['price']
        self.pages = book['pages'] or ''
        self.summary = book['summary'] or ''
        self.image = book['image']
        self.author = ','.join(book['author'])
        self.isbn = book['isbn']
        self.pubdate = book['pubdate']
        self.binding = book['binding']


class BookPage:
    def __init__(self, yushubook:YushuBook):
        self.total = yushubook.total
        self.books = [BookView(book) for book in yushubook.books]
        self.keyword = yushubook.keyword
