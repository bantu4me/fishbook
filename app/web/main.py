from flask import render_template

from .blueprint import web


@web.route('/')
def index():
    return render_template('index.html')


@web.route('/personal')
def personal_center():
    pass