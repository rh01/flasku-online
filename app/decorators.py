# -*- coding:utf-8 -*-
"""
created by Shine at 2017/6/4
"""

from functools import wraps
from flask import abort
from flask_login import current_user
from .models import Permission

def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorator_function(*args, **kwargs):
            if not current_user(permission):
                abort(403)
            return f(*args, **kwargs)
        return decorator_function
    return decorator

def admin_required(f):
    return permission_required(Permission.ADMINISTER)(f)