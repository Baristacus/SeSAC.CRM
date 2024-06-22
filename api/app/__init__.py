from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from app.config import Config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    api = Api(app)

    from app.endpoint.user import UserList, UserDetail

    api.add_resource(UserList, "/api/users")
    api.add_resource(UserDetail, "/api/user/<string:user_id>")

    return app
