# -*- coding:utf-8 -*-
"""
created by: Shenhengheng on 2017/6/4
"""

from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField
from wtforms.validators import Required

class NameForm(FlaskForm):
    name = StringField(label="What's your name?", validators=[Required()])
    submit = SubmitField('Submit')