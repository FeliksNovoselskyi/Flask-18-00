from app.settings import app

try:
    app.run(debug = True)
except:
    print("Ошибка")
