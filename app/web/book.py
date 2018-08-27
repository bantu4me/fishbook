from .blueprint import web


@web.route('/hello')
def hello():
    return 'hello world'
