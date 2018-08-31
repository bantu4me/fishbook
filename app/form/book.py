from wtforms import Form, StringField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange


class SearchForm(Form):
    q = StringField(validators=[DataRequired(message='没有填写搜索条件'), Length(1, 30, message='搜索条件太长')])
    page = IntegerField(validators=[NumberRange(1, 99)], default=1)
