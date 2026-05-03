from app.db import DATABASE
import flask_login as flask_login


# login_manager - менеджер сессий, управляет входом пользователя 
# и поддерживает его действия после логина

class User(DATABASE.Model, flask_login.UserMixin):
    
    id = DATABASE.Column(DATABASE.Integer, primary_key=True)
    email = DATABASE.Column(DATABASE.String)
    password = DATABASE.Column(DATABASE.String)
