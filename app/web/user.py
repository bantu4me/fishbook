from flask import render_template, request

from app import db
from app.form.user import UserRegisterForm
from app.model.user import User
from .blueprint import web


@web.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('auth/login.html', form=[])


@web.route('/register', methods=['GET', 'POST'])
def register():
    form = UserRegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User()
        user.set_attr(form.data)
        with db.auto_commit():
            db.session.add(user)
    return render_template('auth/register.html', form=form)


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    pass


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    pass


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web.route('/logout')
def logout():
    pass
