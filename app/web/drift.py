from flask import render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy import or_, desc

from app import db
from app.form.drift import DriftForm
from app.lib.enums import PendingStatus
from app.lib.utils import send_mail
from app.model.drift import Drift
from app.model.gift import Gift
from app.model.wish import Wish
from app.viewmodel.drift import DriftsViewModel
from app.web.blueprint import web


@web.route('/pending')
@login_required
def pending():
    drifts = Drift.query.filter(
        or_(Drift.requester_id == current_user.id, Drift.gifter_id == current_user.id)).order_by(
        desc(Drift.create_time)).all()
    driftsViewModel = DriftsViewModel(drifts=drifts, uid=current_user.id)
    return render_template('pending.html', drifts=driftsViewModel.drifts)


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
        drift = Drift()
        drift.generate_drift(form, gift, current_user)
        with db.auto_commit():
            # 当前用户鱼豆-1 同时赠送者鱼豆+1
            current_user.beans -= 1
            gift.user.beans += 1
            db.session.add(drift)
            html = render_template('email/get_gift.html', gift=gift, wishername=current_user.nickname)
            send_mail(gift.user.email, html)
            flash('您发送一封邮件给' + gift.user.nickname + ',请等待对方回复')
            return redirect(url_for('web.pending'))
    return render_template('drift.html', gifter=gift.user.summary, form=form, user_beans=current_user.beans)


@web.route('/drift/<int:did>/reject')
def reject_drift(did):
    with db.auto_commit():
        drift = Drift.query.filter_by(gifter_id=current_user.id, id=did).first_or_404()
        drift.pending = PendingStatus.reject
        current_user.beans -= 1
    return redirect(url_for('web.pending'))


@web.route('/drift/<int:did>/redraw')
def redraw_drift(did):
    drift = Drift.query.filter_by(id=did, requester_id=current_user.id).first()
    if drift:
        with db.auto_commit():
            drift.pending = PendingStatus.redraw
            current_user.beans += 1
    return redirect(url_for('web.pending'))


@web.route('/drift/<int:did>/mailed')
def mailed_drift(did):
    drift = Drift.query.filter_by(id=did, gifter_id=current_user.id).first()
    if drift:
        with db.auto_commit():
            drift.pending = PendingStatus.success
            current_user.beans += 1
            gift = Gift.query.filter_by(id=drift.gift_id, launched=False).first_or_404()
            gift.launched = True
            wish = Wish.query.filter_by(isbn=drift.isbn, uid=drift.requester_id, launched=False).first_or_404()
            wish.launched = True
    return redirect(url_for('web.pending'))
