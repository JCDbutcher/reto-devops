from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import config_dict

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_dict[config_name])

    # Inicializar base de datos
    db.init_app(app)

    # Crear tablas si es necesario
    # Descomentar si se quiere auto-crear las tablas al iniciar
    # with app.app_context():
    #     db.create_all()

    # Importar y registrar rutas
    from app.routes import data_routes
    app.register_blueprint(data_routes)

    return app
