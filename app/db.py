import flask_sqlalchemy
import flask_migrate
from .settings import app

# Ключ под которым указывается ссылка на БД
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

data_base = flask_sqlalchemy.SQLAlchemy(app = app)

migrate = flask_migrate.Migrate(
    app = app, # Объект приложения
    db = data_base, # Объект БД
    directory = "app/migrations" # Папка с миграциями (путь к ней)
)