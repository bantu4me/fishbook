from flask import flash, redirect, url_for, render_template
from flask_login import current_user, login_required

from app import db
from app.model.gift import Gift
from app.model.wish import Wish
from app.viewmodel.trade import MyTradesView
from app.web.blueprint import web


@web.route('/my/wish')
@login_required
def my_wish():
    wishes = Wish.my_wish(current_user.id)
    isbn_list = [isbn.book.isbn for isbn in wishes]
    isbn_count_list = Gift.get_gift_cout_by_isbnlist(isbn_list)
    giftsView = MyTradesView(wishes, isbn_count_list)
    return render_template('my_wish.html', wishes=giftsView.trades)


@web.route('/wish/book/<isbn>')
def save_to_wish(isbn):
    can = current_user.can_save_gift_or_wish(isbn)
    if can:
        with db.auto_commit():
            wish = Wish()
            wish.uid = current_user.id
            wish.isbn = isbn
            db.session.add(wish)
            flash('添加到心愿清单成功')
    else:
        flash('本书籍isbn号无效，或者已经添加到您的心愿/礼物清单')
    return redirect(url_for('web.book_detail', isbn=isbn))


@web.route('/satisfy/wish/<int:wid>')
def satisfy_wish(wid):
    pass


@web.route('/wish/book/<isbn>/redraw')
def redraw_from_wish(isbn):
    pass
