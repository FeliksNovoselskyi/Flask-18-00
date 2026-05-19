from home_app.views import render_reg, render_auth, render_logout, render_home
from home_app.app import home_app

from .settings import app

# Flask-SocketIO - библиотека для работы с WebSocket во Flask

home_app.add_url_rule(
    '/',
    view_func=render_home,
    methods = ['GET', 'POST']
)

home_app.add_url_rule(
    '/reg',
    view_func=render_reg,
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