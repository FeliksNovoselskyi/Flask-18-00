import flask
import flask_login as flask_login
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
        email = flask.request.form.get('email')
        password = flask.request.form.get('password')
        
        if email and password :
            user = User.query.filter_by(email = email).scalar()
            
            password_correct = security.check_password_hash(pwhash = user.password, password = password)
            
            if password_correct:
                flask_login.login_user(user)
                
    return flask.render_template("auth.html")
