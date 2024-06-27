from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(BASE_DIR, "database3.db")
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"

    db.init_app(app)

    from .views import main, user, store, item, order, orderitem

    app.register_blueprint(main.bp)
    app.register_blueprint(user.bp)
    app.register_blueprint(store.bp)
    app.register_blueprint(item.bp)
    app.register_blueprint(order.bp)
    app.register_blueprint(orderitem.bp)

    def format_datetime(value, fmt="%Y년 %m월 %d일 %H시 %M분 %S초"):
        return value.strftime(fmt)

    def format_date(value, fmt="%Y년 %m월 %d일"):
        return value.strftime(fmt)

    app.jinja_env.filters["date"] = format_date
    app.jinja_env.filters["datetime"] = format_datetime

    return app
