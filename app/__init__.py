from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_cors import CORS
from config import Config

db = SQLAlchemy()
api = Api()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    api.init_app(app)
    CORS(app)

    from .routes import initialize_routes
    initialize_routes(api)

    return app
