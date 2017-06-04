# -*- coding:utf-8 -*-
"""
created by: Shenhengheng on 2017/6/4
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField,BooleanField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from ..models import User
from wtforms import ValidationError


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Required(), Length(1,64),
                                             Email()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me Login in')
    submit = SubmitField('Log in')


class RegistrationForm(FlaskForm):
    email = StringField('Email',validators=[Required(), Length(1,64),
                                            Email()])
    username = StringField('Username', validators=[Required(),
                                                   Length(1, 64),
                                                   Regexp('^[A-Za-z][A-Za-z0-9_.]*$',
                                                   0,
                                                   'Username must have only letters,'
                                                   'numbers , dots or underscores')])
    password = PasswordField('Password',validators=[
        Required(),EqualTo('password2', message='password must match.')
    ])

    password2 = PasswordField('Confirm password',validators=[Required()])
    submit = SubmitField('Register')

    def validate_email(self, filed):
        if User.query.filter_by(email=filed.data).first():
            raise ValidationError('Email already registered')


    def validate_username(self, filed):
        if User.query.filter_by(username=filed.data):
            ValidationError('Usernamse already in use')