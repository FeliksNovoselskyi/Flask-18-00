from home_app.views import render_home
from home_app.app import home_app

from .settings import app

home_app.add_url_rule(
    '/',
    view_func=render_home,
)

app.register_blueprint(home_app)