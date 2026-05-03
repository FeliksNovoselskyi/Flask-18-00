"""
Модуль с настройками login_manager
"""

import flask_login
from home_app.models import User
from .settings import app

app.secret_key = ""

manager = flask_login.LoginManager(
    app
)

# Декоратор - это функция которая модифицирует другую функцию
# Декораторы пишутся с @

@manager.user_loader
def get_user(user_id):
    return User.query.get(user_id)


