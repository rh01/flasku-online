# -*- coding:utf-8 -*-
"""
created by: Shenhengheng on 2017/6/4
"""
from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors