import flask_socketio
from app.settings import socket
from .models import Message
from app.db import DATABASE as DB


# Дописать обработку события connect

@socket.on("connect")
def func():
    print('Вы подключились')
    
    socket.emit(
        "message", 
        {
            "message_text": "Soodsenie"
        }
    )

@socket.on("disconnect")
def func1():
    print('Вы отключились')



@socket.on("message")
def func2(data):
    
    print("\n", data, "\n")
    
    message = Message(
        text = data["messagetext"]
    )
    
    DB.session.add(message)
    DB.session.commit()




# @socket.on('join_room')
# def function():
    
#     flask_socketio.join_room('room1')
    
#     socket.emit('join_room', {'room': 'room1'}, to = "room1")
    
#     # в to указываем клиента/комнату в которую отправить событие
    