import flask
import flask_sqlalchemy
import flask_migrate

from .settings import app

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"

DATABASE = flask_sqlalchemy.SQLAlchemy(app = app)


migrate = flask_migrate.Migrate(
    app = app,
    db = DATABASE,
    directory= "app/migrations"
)
