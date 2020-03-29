from config import app_config
from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()


def create_app_contact_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    db.init_app(app)
    migrate.init_app(app, db)

    manager = Manager(app)
    manager.add_command('db', MigrateCommand)

    from contact_app.views import load_contact_views
    load_contact_views(app, db)

    return app
