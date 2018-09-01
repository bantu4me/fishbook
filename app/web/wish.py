from flask import flash, redirect, url_for
from flask_login import current_user

from app import db
from app.model.wish import Wish
from app.web.blueprint import web


@web.route('/my/wish')
def my_wish():
    pass


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
