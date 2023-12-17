from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import Length, DataRequired, Email


class PostForm(FlaskForm):
    title = StringField('title', validators=[Length(max=120), DataRequired()])
    body = StringField('body')


class SignupForm(FlaskForm):
    name = StringField('name', validators=[Length(max=100), DataRequired()])
    username = StringField('username', validators=[Length(max=100), DataRequired()])
    email = StringField('email', validators=[Length(max=120)])
    password = StringField('password', validators=[Length(min=4)])


class LoginForm(FlaskForm):
    email = StringField('email', validators=[Length(max=120)])
    password = StringField('password', validators=[Length(min=4)])
