# -*- coding:utf-8 -*-
"""
created by: Shenhengheng on 2017/6/4
"""
from flask import Blueprint
from ..models import Permission


main = Blueprint('main', __name__)

from . import views, errors

@main.app_context_processor
def injet_permissions():
    return dict(Permission=Permission)