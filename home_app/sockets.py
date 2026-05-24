import flask_socketio
from app.settings import socket

@socket.on("connect")
def handle_connect():
    print("Вы подключились")
    


