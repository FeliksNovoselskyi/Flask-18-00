import flask
from .models import User
from app.db import DATABASE




def render_home():
    print(flask.request.method)
    
    if flask.request.method == "POST":
        email = flask.request.form.get("email")
        password = flask.request.form.get("password")
        confirm_password = flask.request.form.get("confirm_password")
        print(email, password, confirm_password)
        
        if email and password and confirm_password:
            if password == confirm_password:
                user = User(
                    email = email,
                    password = password
                )
                DATABASE.session.add(user)
                DATABASE.session.commit()
    return flask.render_template("home.html")
