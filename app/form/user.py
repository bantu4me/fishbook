from wtforms import Form, StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError, StopValidation

from app.model.user import User


class UserLoginForm(Form):
    email = StringField(validators=[DataRequired('请填写邮箱账号'), Email('格式不符合规范')])
    password = PasswordField(validators=[DataRequired('请输入密码'), Length(6, 30, '密码长度不符合规范')])


class UserRegisterForm(Form):
    email = StringField(validators=[DataRequired('请填写邮箱账号'), Email('格式不符合规范')])
    nickname = StringField(validators=[DataRequired('请输入昵称'), Length(1, 20, '昵称长度不符合规范')])
    password = PasswordField(validators=[DataRequired('请输入密码'), Length(6, 30, '密码长度不符合规范')])
    confirm = PasswordField(validators=[DataRequired('请确认密码'), EqualTo('password', '两次输入的密码不一致')])

    def validate_email(self, field):
        user = User.query.filter_by(email=field.data).first()
        if user:
            # raise ValidationError(message='该邮箱已被注册')
            raise StopValidation(message='该邮箱已被注册')


class ForgetPwdForm(Form):
    email = StringField(validators=[DataRequired('请输入你的注册邮箱'), Email('邮箱格式不符合规范')])
