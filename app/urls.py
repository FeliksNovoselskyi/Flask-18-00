from home_app.views import render_home, render_auth, render_logout
from home_app.app import home_app

from .settings import app

home_app.add_url_rule(
    '/',
    view_func=render_home,
    methods = ['GET', 'POST']
)

home_app.add_url_rule(
    "/auth",
    view_func = render_auth,
    methods = ["GET", "POST"]
)


home_app.add_url_rule(
    "/logout",
    view_func = render_logout,
    methods = ["GET", "POST"]
)


app.register_blueprint(home_app)