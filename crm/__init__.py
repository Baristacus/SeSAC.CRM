from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(BASE_DIR, "database.db")
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"

    db.init_app(app)

    from .views import main, user, store, item, order, orderitem

    app.register_blueprint(main.bp)
    app.register_blueprint(user.bp)
    app.register_blueprint(store.bp)
    app.register_blueprint(item.bp)
    app.register_blueprint(order.bp)
    app.register_blueprint(orderitem.bp)

    return app