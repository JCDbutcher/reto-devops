from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from app.config import config_dict

# Inicialización de SQLAlchemy (se usará más adelante con el objeto Flask)
db = SQLAlchemy()

# Definición del blueprint para las rutas (ruta principal /)
data_routes = Blueprint('data_routes', __name__)

@data_routes.route('/', methods=['GET'])
def home():
    """Ruta raíz que devuelve un mensaje de bienvenida en formato JSON."""
    return jsonify({"message": "Bienvenido a la API"})

def create_app(config_name):
    """
    Función de fábrica para crear y configurar una aplicación Flask.

    Args:
        config_name (str): nombre de la configuración a usar (development, testing, production)

    Returns:
        app (Flask): instancia de la aplicación Flask configurada
    """
    app = Flask(__name__)
    
    # Cargar configuración desde el diccionario según el entorno (config.py)
    app.config.from_object(config_dict[config_name])

    # Inicializar la extensión de base de datos con la app
    db.init_app(app)

    # Crear las tablas de la base de datos si fuera necesario (opcional)
    # with app.app_context():
    #     db.create_all()

    # Importar y registrar las rutas definidas en el archivo routes.py
    from app.routes import data_routes
    app.register_blueprint(data_routes)

    return app
