# -*- coding:utf-8 -*-
"""
created by: Shenhengheng on 2017/6/4
"""
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = '465'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <m18317774480@163.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    FLASKY_POSTS_PER_PAGE = 20
    FLASKY_FOLLOWERS_PER_PAGE = 50
    FLASKY_COMMENTS_PER_PAGE = 20


    @staticmethod
    def init_app():
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:hadoop@127.0.0.1:3306/flasky'

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:hadoop@127.0.0.1:3306/flasky_test'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:hadoop@127.0.0.1:3306/flasky_product'

# class DevelopmentConfig(Config):
#
#
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATAVASE_URL') or\
#                               'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
#
#
# class TestingConfig(Config):
#     TESTING = True
#
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATAVASE_URL') or \
#                               'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')
#
# class ProductionConfig(Config):
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATAVASE_URL') or \
#                               'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig,
}


