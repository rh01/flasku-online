# -*- coding:utf-8 -*-
"""
created by: Shenhengheng on 2017/6/4
"""

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

from config import config

# initialize the
bootstrap = Bootstrap()
moment = Moment()
mail = Mail()
db = SQLAlchemy()

def create_app(config_name):
    from .main import main as main_blueprint

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.register_blueprint(main_blueprint)
    config[config_name].init_app()

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    return app

