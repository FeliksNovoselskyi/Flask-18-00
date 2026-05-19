from app.settings import app, socket


try:
    # Запускаем сокет сервер
    socket.run(
        app=app, 
        debug = True, 
        port = 8001
    )
    
except:
    print("Ошибка")
