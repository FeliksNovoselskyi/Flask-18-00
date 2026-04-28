from app.settings import app

try:
    app.run(debug = True, port = 8001)
except:
    print("Ошибка")
