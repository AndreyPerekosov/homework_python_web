from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import Length, DataRequired


class PostForm(FlaskForm):
    title = StringField('title', validators=[Length(max=120), DataRequired()])
    body = StringField('body')