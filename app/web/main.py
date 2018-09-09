from flask import render_template
from flask_login import login_required, current_user

from app.model.gift import Gift
from app.viewmodel.book import BookView
from app.viewmodel.user import PersonView
from .blueprint import web


@web.route('/')
def index():
    recent_gift = Gift.get_recent()
    recent = [BookView(recent.get_book_dict()) for recent in recent_gift]
    return render_template('index.html', recent=recent)


@web.route('/personal')
@login_required
def personal_center():
    user = PersonView(current_user)
    return render_template('personal.html', user=user)
