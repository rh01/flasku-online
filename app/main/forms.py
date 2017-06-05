# -*- coding:utf-8 -*-
"""
created by: Shenhengheng on 2017/6/4
"""

from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField, TextAreaField
from wtforms.validators import Required,Length

class NameForm(FlaskForm):
    name = StringField(label="What's your name?", validators=[Required()])
    submit = SubmitField('Submit')


class EditProfileForm(FlaskForm):
    name = StringField('Real name', validators=[Length(1,64)])
    location = StringField('location', validators=[Length(0,64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')

class PostForm(FlaskForm):
    body = TextAreaField("What's on your mind?", validators=[Required()])
    submit = SubmitField('Submit')
