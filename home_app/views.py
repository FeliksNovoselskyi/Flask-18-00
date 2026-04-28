import flask

# Модуль для с хешированием
import werkzeug.security as security

from .models import User
from app.db import DATABASE


def render_home():

    if flask.request.method == "POST":
        email = flask.request.form.get("email")
        password = flask.request.form.get("password")
        confirm_password = flask.request.form.get("confirm_password")
        
        if email and password and confirm_password:
            if password == confirm_password:
                
                hash_pasword = security.generate_password_hash(password= password)
                
                user = User (email = email, password = hash_pasword)

                DATABASE.session.add(user)
                DATABASE.session.commit()
                
    return flask.render_template("home.html")



def render_auth():
    
    if flask.request.method == "POST":
        email = flask.request.form.get("email")
        password = flask.request.form.get("password")
        
        if email and password:
            
            user1 = User.query.filter_by(email = email).scalar()
            print(user1)
            
    
    return flask.render_template("auth.html")
