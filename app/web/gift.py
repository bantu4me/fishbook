from flask import flash, render_template, redirect, url_for
from flask_login import login_required, current_user

from app import db
from app.model.gift import Gift
from app.web.blueprint import web


@web.route('/my/gifts')
@login_required
def my_gifts():
    pass


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gift(isbn):
    can = current_user.can_save_gift_or_wish(isbn)
    if can:
        with db.auto_commit():
            gift = Gift()
            gift.uid = current_user.id
            gift.isbn = isbn
            db.session.add(gift)
            flash('添加到礼物清单成功')
    else:
        flash('本书籍isbn号无效，或者已经添加到您的心愿/礼物清单')
    return redirect(url_for('web.book_detail', isbn=isbn))


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass
