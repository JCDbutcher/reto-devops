from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import config_dict

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_dict[config_name])

    # Initialize the database
    db.init_app(app)

 #   with app.app_context():
 #       db.create_all()  # <-- Esta línea crea las tablas si no existen

    # Import blueprints/routes
    from app.routes import data_routes

    # Register blueprints
    app.register_blueprint(data_routes)

    return app

