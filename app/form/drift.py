from wtforms import Form, StringField
from wtforms.validators import DataRequired, Length


class DriftForm(Form):
    recipient_name = StringField(validators=[DataRequired('请填写收件人姓名')])
    mobile = StringField(validators=[DataRequired('请填写练习电话')])
    address = StringField(validators=[DataRequired('请填写收件地址'), Length(6, 100, '请填写详细地址')])
    message = StringField()
