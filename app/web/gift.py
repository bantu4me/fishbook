from flask_login import login_required

from app.web.blueprint import web


@web.route('/my/gifts')
def my_gifts():
    pass


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gift(isbn):
    return 'save_to_gift'


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass
