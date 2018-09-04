from flask import render_template, request
from flask_login import current_user

from app.form.book import SearchForm
from app.model.gift import Gift
from app.model.wish import Wish
from app.viewmodel.book import BookPage, BookView
from app.viewmodel.trade import TradesView
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

    ##############################
    has_in_wishes = False
    has_in_gifts = False
    giftsView = []
    wishesView = []

    # 当前用户已经登录
    if current_user and current_user.is_authenticated:
        wish = Wish.query.filter_by(isbn=isbn, launched=False, uid=current_user.id).first()
        gift = Gift.query.filter_by(isbn=isbn, launched=False, uid=current_user.id).first()

        if wish or (not wish and not gift):
            has_in_wishes = True
            gifts = Gift.query.filter_by(isbn=isbn, launched=False).all()
            giftsView = TradesView(gifts)

        if gift:
            has_in_gifts = True
            wishes = Wish.query.filter_by(isbn=isbn, launched=False).all()
            wishesView = TradesView(wishes)
    else:
        gifts = Gift.query.filter_by(isbn=isbn, launched=False).all()
        giftsView = TradesView(gifts)

    return render_template('book_detail.html', book=book, gifts=giftsView,
                           wishes=wishesView, has_in_wishes=has_in_wishes, has_in_gifts=has_in_gifts)
