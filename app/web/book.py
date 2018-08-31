from flask import render_template, request

from app.form.book import SearchForm
from app.viewmodel.book import BookPage
from .blueprint import web
from app.lib.utils import is_isbn_or_key
from app.lib.yushu_book import YushuBook


@web.route('/book/search')
def search():
    form = SearchForm(request.args)
    if form.validate():
        yushubook = YushuBook()
        isbn_or_key = is_isbn_or_key(form.q.data)
        if isbn_or_key == 'key':
            yushubook.search_by_keyword(form.q.data, form.page.data)
        books = BookPage(yushubook)
    return render_template('search_result.html', books=books, form=form)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    pass
