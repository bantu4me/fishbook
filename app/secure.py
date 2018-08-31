# 调试模式
DEBUG = False
HOST = '0.0.0.0'
PORT = 5000

# db
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:root@localhost:3306/fishbook'

# 书籍请求地址
ISBN_URL = 'http://t.yushu.im/v2/book/isbn/{}'
KEYWORD_URL = 'http://t.yushu.im/v2/book/search?q={}&start={}&count={}'
# 分页数量
PER_PAGE = 15