
"""
Модуль с настройками login_manager
"""

import flask_login
from home_app.models import User
from .settings import app
from config import SECRET_KEY

from flask_login import LoginManager


app.secret_key = SECRET_KEY

login_manager = LoginManager(app)

@login_manager.user_loader
def get_user(user_id):
    return User.query.get(user_id)
