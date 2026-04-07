import flask
from flask import Blueprint

home_app = flask.Blueprint(
    name= "home_app",
    import_name= "home_app",
    template_folder= "templates",
    static_folder= "static"
)