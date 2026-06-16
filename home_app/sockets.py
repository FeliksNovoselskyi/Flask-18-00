import flask
import flask_login
import flask_socketio
from app.settings import socket
from .models import Group
from app.db import DATABASE as DB
from .app import online_users


# Дописать обработку события connect
@socket.on("connect")
def func():
    print('Вы подключились')
    
    user_id = flask_login.current_user.id
    
    
    if user_id in online_users:
        online_users[user_id].add(flask.request.sid)
    else:
        online_users[user_id] = set()
        online_users[user_id].add(flask.request.sid)
    
    # Получаем данные пользователей
    group = Group.query.get(1)
    data = {
        "title" : group.group_name,
        "members": []
    }
    
    users = group.users
    
    for user in users:
        
        if user.id in online_users.keys():
            status = "✅ ON line 📗"
        else:
            status = "❌ OFF line 📕"

        data['members'].append({
            "status": status,
            'email': user.email
        })
    
    socket.emit("display_status", data)
    

@socket.on("disconnect")
def func1():
    
    user_id = flask_login.current_user.id
    
    online_users[user_id].discard(flask.request.sid)
    
    # Проверить равен ли set объект пустому сету (set())
    if online_users[user_id] == set():
        del online_users[user_id]
        # Удаляем set объект
    
    print('Вы отключились')
    
    print("\n DISCONNECT:", online_users, "\n")
    
    # Получаем данные пользователей
    group = Group.query.get(1)
    data = {
        "title" : group.group_name,
        "members": []
    }
    
    users = group.users
    
    
    """
    {
        1: {
            "123123",
        },
        2: {}
    }
    """
    
    for user in users:
        
        if user.id in online_users.keys():
            status = "✅ ON line 📗"
        else:
            status = "❌ OFF line 📕"

        data['members'].append({
            "status": status,
            'email': user.email
        })
    
    socket.emit("display_status", data)

@socket.on("message")
def func123():
    print("СОБЫТИЕ")

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




socket.emit("event2")
