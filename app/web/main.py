from flask import render_template

from app.model.gift import Gift
from app.viewmodel.book import BookView
from .blueprint import web


@web.route('/')
def index():
    recent_gift = Gift.get_recent()
    recent = [BookView(recent.get_book_dict()) for recent in recent_gift]
    return render_template('index.html', recent=recent)


@web.route('/personal')
def personal_center():
    pass
