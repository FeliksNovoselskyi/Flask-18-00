import flask
import flask_login
import werkzeug.security as security
from .models import Group
from .models import User
from app.db import DATABASE


def render_home():
    
    group = Group.query.get(1)
    slovar = {
        "title" : group.group_name,
        "members": []
    }
    
    users = group.users
    
    for user in users:
        slovar["members"].append({"email": user.email})
    
    # **dict - распаковывают
    
    return flask.render_template("home.html", **slovar)


def render_reg():
    
    print(flask_login.current_user.is_authenticated)
    
    if flask_login.current_user.is_authenticated:
        return flask.render_template("reg.html", aboba123 = True)
    
    if flask.request.method == "POST":
        email = flask.request.form.get("email")
        password = flask.request.form.get("password")
        confirm_password = flask.request.form.get("confirm_password")
        
        if email and password and confirm_password:
            if password == confirm_password:
                
                hash_pasword = security.generate_password_hash(password= password)
                
                user = User (email = email, password_hash = hash_pasword)

                DATABASE.session.add(user)
                DATABASE.session.commit()
            
            
    return flask.render_template("reg.html")



def render_auth():
    
    if flask.request.method == "POST":
        email = flask.request.form.get('email')
        password = flask.request.form.get('password')
        
        if email and password :
            user = User.query.filter_by(email = email).scalar()
            
            hashed_checked_password = security.check_password_hash(pwhash = user.password_hash, password = password)

            if hashed_checked_password == True:
                flask_login.login_user(user)
    
    return flask.render_template("auth.html")


def render_logout():
    
    flask_login.logout_user()
    
    return flask.redirect("/auth")
