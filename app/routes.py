from flask import Blueprint, request, jsonify
from app.models import Data
from app import db

# Definición del blueprint para agrupar las rutas relacionadas con 'data'
data_routes = Blueprint("data_routes", __name__)


@data_routes.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Bienvenido a la API"})


@data_routes.route("/data", methods=["POST"])
def insert_data():
    data = request.json
    name = data.get("name")

    if not name:
        return jsonify({"message": "El campo 'name' es obligatorio"}), 400

    existing_data = Data.query.filter_by(name=name).first()
    if existing_data:
        return jsonify({"message": "El dato ya existe"}), 409

    new_data = Data(name=name)
    db.session.add(new_data)
    db.session.commit()

    return jsonify({"message": "Dato insertado correctamente"}), 201


@data_routes.route("/data", methods=["GET"])
def get_all_data():
    data_list = [{"id": data.id, "name": data.name} for data in Data.query.all()]
    return jsonify(data_list)


@data_routes.route("/data/<int:id>", methods=["DELETE"])
def delete_data(id):
    element = Data.query.get(id)
    if not element:
        return jsonify({"message": "Dato no encontrado"}), 404

    db.session.delete(element)
    db.session.commit()

    return jsonify({"message": "Dato eliminado correctamente"}), 200
