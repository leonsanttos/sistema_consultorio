from flask import Flask

from app import database
from app.config import Config
from app.routes import register_blueprints


def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object(Config)
    if config:
        app.config.update(config)

    database.init_app(app)
    register_blueprints(app)
    return app
