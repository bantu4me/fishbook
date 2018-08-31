from flask import render_template, request

from app.form.book import SearchForm
from app.viewmodel.book import BookPage, BookView
from .blueprint import web
from app.lib.utils import is_isbn_or_key
from app.lib.yushu_book import YushuBook


@web.route('/book/search')
def search():
    form = SearchForm(request.args)
    books = BookPage()
    if form.validate():
        yushubook = YushuBook()
        isbn_or_key = is_isbn_or_key(form.q.data)
        if isbn_or_key == 'key':
            yushubook.search_by_keyword(form.q.data, form.page.data)
        else:
            yushubook.search_by_isbn(form.q.data)
        books.fill_book_page(yushubook)
    return render_template('search_result.html', books=books, form=form)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    yushubook = YushuBook()
    yushubook.search_by_isbn(isbn)
    book = BookView(yushubook.only)
    return render_template('book_detail.html', book=book, gifts=[], wishes=[])