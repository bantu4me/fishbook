# 调试模式
DEBUG = False
HOST = '0.0.0.0'
PORT = 5000

# db
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:root@localhost:3306/fishbook'

# 书籍请求地址
isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
keyword_url = 'http://t.yushu.im/v2/book/search?q={}&start={}&count={}'
