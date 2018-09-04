from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
'''
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TSL = False
MAIL_USERNAME = 'lijie9306f@qq.com'
MAIL_PASSWORD = 'dmzwwiqhbuuybfde'
'''
app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SS'] = True
app.config['MAIL_USE_TSL'] = False
app.config['MAIL_PASSWORD'] = 'dmzwwiqhbuuybfde'

mail = Mail(app)

msg = Message("Hello",
              sender="lijie9306f@qq.com",
              recipients=["jetlee1906@163.com"])
msg.body = '这是一封测试邮件'

if __name__ == '__main__':
    with app.app_context():
        mail.send(msg)
