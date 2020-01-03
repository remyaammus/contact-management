# third-party imports
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# local imports
from config import app_config

# db variable initialization
db = SQLAlchemy()


def create_app_contact_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    db.init_app(app)
    migrate = Migrate(app, db)

    from contact_app import models

    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    return app
