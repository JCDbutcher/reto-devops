from flask import Blueprint, request, jsonify
from app.models import Data
from app import db

# Definición del blueprint para agrupar las rutas relacionadas con 'data'
data_routes = Blueprint("data_routes", __name__)

# Ruta principal de bienvenida
@data_routes.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Bienvenido a la API"})

# Ruta para insertar un nuevo dato
@data_routes.route("/data", methods=["POST"])
def insert_data():
    data = request.json  # Se espera que los datos se envíen en formato JSON
    name = data.get("name")

    if not name:
        return jsonify({"message": "El campo 'name' es obligatorio"}), 400

    # Verificar si ya existe un dato con ese nombre
    existing_data = Data.query.filter_by(name=name).first()
    if existing_data:
        return jsonify({"message": "El dato ya existe"}), 409

    # Crear y guardar nuevo dato
    new_data = Data(name=name)
    db.session.add(new_data)
    db.session.commit()

    return jsonify({"message": "Dato insertado correctamente"}), 201

# Ruta para obtener todos los datos
@data_routes.route("/data", methods=["GET"])
def get_all_data():
    data_list = [{"id": data.id, "name": data.name} for data in Data.query.all()]
    return jsonify(data_list)

# Ruta para eliminar un dato por ID
@data_routes.route("/data/<int:id>", methods=["DELETE"])
def delete_data(id):
    element = Data.query.get(id)
    if not element:
        return jsonify({"message": "Dato no encontrado"}), 404

    db.session.delete(element)
    db.session.commit()
    return jsonify({"message": "Dato eliminado correctamente"}), 200
