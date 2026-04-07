from home_app import home_app, render_home
from .settings import app

home_app.add_url_rule(
    '/',
    view_func=render_home,
)

app.register_blueprint(home_app)