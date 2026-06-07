import flask
import flask_login
import flask_socketio
from app.settings import socket
from .models import Message, Group
from app.db import DATABASE as DB
from .app import online_users


# Дописать обработку события connect
@socket.on("connect")
def func():
    print('Вы подключились')
    
    user_id = flask_login.current_user.id
    
    {
        
    }
    
    if user_id not in online_users.keys():
        online_users[user_id] = set()
    
    online_users[user_id].add(flask.request.sid)
    
    
    
    print("\n", online_users, "\n")

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
