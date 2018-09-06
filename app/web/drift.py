from flask import render_template, request, flash
from flask_login import login_required, current_user

from app.form.drift import DriftForm
from app.model.gift import Gift
from app.web.blueprint import web


@web.route('/pending')
def pending():
    return render_template('pending.html')


@web.route('/drift/<int:gid>', methods=['GET', 'POST'])
@login_required
def send_drift(gid):
    form = DriftForm(request.form)
    gift = Gift.query.filter_by(id=gid).first()
    if not gift:
        flash('没有人赠送该本书籍，请确认')
    my_gift = Gift.query.filter_by(id=gid, uid=current_user.id).first()
    if my_gift:
        flash('这部书是您自己赠送的，不能向他人请求')
    can_send_drift = current_user.can_send_drift()
    if not can_send_drift:
        return render_template('not_enough_beans.html', beans=current_user.beans)
    if request.method == 'POST' and form.validate():
        pass
    return render_template('drift.html', gifter=gift.user.summary, form=form, user_beans=current_user.beans)


@web.route('/drift/<int:did>/reject')
def reject_drift(did):
    pass


@web.route('/drift/<int:did>/redraw')
def redraw_drift(did):
    pass


@web.route('/drift/<int:did>/mailed')
def mailed_drift(did):
    pass
