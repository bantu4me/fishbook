from flask import flash, redirect, url_for, render_template
from flask_login import current_user, login_required

from app import db
from app.lib.utils import send_mail
from app.model.gift import Gift
from app.model.wish import Wish
from app.viewmodel.trade import MyTradesView
from app.web.blueprint import web


@web.route('/my/wish')
@login_required
def my_wish():
    wishes = Wish.my_wish(current_user.id)
    isbn_list = [isbn.book.isbn for isbn in wishes]
    trades = []
    if len(isbn_list) > 0:
        isbn_count_list = Gift.get_gift_cout_by_isbnlist(isbn_list)
        trades = MyTradesView(wishes, isbn_count_list).trades
    return render_template('my_wish.html', wishes=trades)


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
@login_required
def satisfy_wish(wid):
    wish = Wish.query.get_or_404(wid)
    gift = Gift.query.filter_by(uid=current_user.id, isbn=wish.isbn).first()
    if not gift:
        flash('你还没有上传此书，请点击“加入到赠送清单”添加此书。添加前，请确保自己可以赠送此书')
    else:
        html = render_template('email/satisify_wish.html', wish=wish, gift=gift)
        send_mail(wish.user.email,html,subject='[有人想送你一本书]')
        flash('已向他/她发送了一封邮件，如果他/她愿意接受你的赠送，你将收到一个鱼漂')
    return redirect(url_for('web.book_detail', isbn=wish.isbn))


@web.route('/wish/book/<isbn>/redraw')
@login_required
def redraw_from_wish(isbn):
    wish = Wish.query.filter_by(uid=current_user.id, isbn=isbn, launched=False).first()
    if wish:
        with db.auto_commit():
            wish.delete()
            flash_msg = '撤销书籍《' + wish.book.title + '》成功'
            flash(flash_msg)
    else:
        flash('书籍不存在')
    return redirect(url_for('web.my_wish'))
