from flask import Flask, Blueprint, jsonify
from flask_sqlalchemy import SQLAlchemy
from app.config import config_dict

# Inicialización global de SQLAlchemy
db = SQLAlchemy()

# Blueprint para ruta básica (puede eliminarse si está duplicado en routes.py)
data_routes = Blueprint('data_routes', __name__)


@data_routes.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Bienvenido a la API"})


def create_app(config_name):
    """
    Crea y configura la aplicación Flask.
    """
    app = Flask(__name__)
    app.config.from_object(config_dict[config_name])

    # Inicializar extensión SQLAlchemy
    db.init_app(app)

    # Importar y registrar rutas del módulo
    from app.routes import data_routes
    app.register_blueprint(data_routes)

    return app
