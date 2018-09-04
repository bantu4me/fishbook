# 调试模式
DEBUG = False
HOST = '0.0.0.0'
PORT = 5000

# 设置secret key
SECRET_KEY = '\x13\x7f\x02\xf6\xcb:\x95\xd9\xb8\xdb:\x8ba\xa5\x07\xdd\x8e\xb6\xcb\x8e\xe3I\x97\x1c'

# db
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:root@localhost:3306/fishbook'

# 书籍请求地址
ISBN_URL = 'http://t.yushu.im/v2/book/isbn/{}'
KEYWORD_URL = 'http://t.yushu.im/v2/book/search?q={}&start={}&count={}'
# 分页数量
PER_PAGE = 15

# 邮件配置
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TSL = False
MAIL_USERNAME = 'lijie9306f@qq.com'
MAIL_PASSWORD = 'dmzwwiqhbuuybfde'
