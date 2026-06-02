import flask
import flask_socketio
from app.settings import socket
from .models import Message, Group
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



@socket.on('join_room')
def function(data: dict):
    
    group_id = data["groupId"]
    user_id = data["userId"]
    
    group = Group.query.get(group_id) # 15
    
    if group:
        if user_id in group.users:
            flask_socketio.join_room(f'room_{group.id}')
            
            socket.emit(
                'join_room', 
                {
                    'room': 'room1',
                    "message": 'Подключился клиент в комнату'
                }, 
                to = "room1"
            )
            
            flask.request.sid
            
            # в to указываем клиента/комнату в которую отправить событие


# Обработать событие leave_room
@socket.on('leave_room')
def handle_leave_room():

    flask_socketio.leave_room('room1')

    socket.emit('leave_room', {'room': 'room1'}, to = "room1")
