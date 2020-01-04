from config import app_config
from flask import Flask, render_template
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

    from contact_app.models import Contact

    @app.route('/')
    def contact_list_view():
        all_contacts = Contact.query.all()
        return render_template('contact_list.html', all_contacts=all_contacts)
        #
        # from random import randint
        # admin = Contact(id=randint(1, 1000000), email='admindfasdf@example.com')
        # db.session.add(admin)
        # db.session.commit()
        # return 'Hello, World!'

    @app.route('/<contact_id>')
    def contact_detail_view(contact_id):
        contact = Contact.query.filter_by(id=contact_id).first()
        return render_template('contact_details.html', contact=contact)

    return app
