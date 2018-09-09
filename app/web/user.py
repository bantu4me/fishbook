from flask import render_template, request, redirect, url_for, flash, current_app
from flask_login import login_user, current_user, logout_user

from app import db
from app.form.user import UserRegisterForm, UserLoginForm, ForgetPwdForm, ForgetPwsRequestForm
from app.lib.utils import send_mail
from app.model.user import User
from .blueprint import web
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired


@web.route('/login', methods=['GET', 'POST'])
def login():
    form = UserLoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_pwd(form.password.data):
            login_user(user)
            next = request.args.get('next')
            if not next or not next.startswith('/'):
                next = url_for('web.index')
            return redirect(next)
        else:
            flash(message='用户名或密码错误')
    return render_template('auth/login.html', form=form)


@web.route('/register', methods=['GET', 'POST'])
def register():
    form = UserRegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User()
        user.set_attr(form.data)
        with db.auto_commit():
            db.session.add(user)
        return redirect(url_for('web.login'))
    return render_template('auth/register.html', form=form)


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    form = ForgetPwdForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            html = render_template('email/reset_password.html', user=user, token=user.generate_token())
            send_mail(form.email.data, html)
        else:
            flash('账号不存在')
    return render_template('auth/forget_password_request.html', form=form)


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    try:
        s = Serializer(secret_key=current_app.config['SECRET_KEY'])
        form = ForgetPwsRequestForm(request.form)
        if request.method == 'POST' and form.validate():
            info = s.loads(token)
            if info and info.get('id') and info.get('email'):
                user = User.query.filter_by(id=info.get('id'), email=info.get('email')).first()
                if user:
                    with db.auto_commit():
                        user.password = form.password1.data
                        flash('更新密码成功，请使用新密码登录')
                    return redirect(url_for('web.login'))
                else:
                    flash('没有这个用户')
                    return redirect(url_for('web.index'))
    except SignatureExpired:
        flash('token已经超时,请重新向服务器请求')
    finally:
        return render_template('auth/forget_password.html')


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web.route('/logout')
def logout():
    if current_user and current_user.is_authenticated:
        logout_user()
    else:
        flash('您还没有登录账户')
    return redirect(url_for('web.index'))
