from .blueprint import web


@web.route('/login')
def login():
    return 'user login'
