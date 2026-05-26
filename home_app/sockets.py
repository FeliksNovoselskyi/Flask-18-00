import flask_socketio
from app.settings import socket
from .models import Message
from app.db import DATABASE as DB

# Дописать обработку события connect

@socket.on("connect")
def func():
    print('Вы подключились')
    
    message1 = Message.query.get(1)

    socket.emit(
        "message", 
        {
            "from": "Feliks",
            "message_text": message1.text
        }
    )

@socket.on("disconnect")
def func1():
    print('Вы отключились')



# @socket.on("message")
# def func2(data):
    
#     message = Message(
#         text = data["messagetext"]
#     )
    
#     DB.session.add(message)
#     DB.session.commit()

