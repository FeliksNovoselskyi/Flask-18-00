import flask

home_app = flask.Blueprint(
    name= "home_app",
    import_name= "home_app",
    template_folder= "templates",
    static_folder= "static",
    static_url_path="/home_app/static"
)

online_users = {}


"""
{
    1: {
        "123123",
        "123123"
    },
    2: {}
}

"""

