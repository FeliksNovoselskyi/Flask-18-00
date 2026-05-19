
import flask, os
import flask_socketio

app = flask.Flask(
    import_name = "app",
    instance_path = os.path.abspath(os.path.join(__file__, "..", "instance"))
)

# Объект сокета
socket = flask_socketio.SocketIO(
    app = app
)

