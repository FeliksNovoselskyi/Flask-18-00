
import flask, os

app = flask.Flask(
    import_name = "app",
    instance_path = os.path.abspath(os.path.join(__file__, "..", "instance"))
)
