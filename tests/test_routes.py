import pytest
from app import create_app, db
from app.models import Data


@pytest.fixture
def client():
    # Configura y crea la app en modo de testing con DB en memoria
    app = create_app('testing')
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.app_context():
        db.create_all()  # Crea las tablas necesarias

    # Cliente de pruebas para hacer peticiones HTTP
    with app.test_client() as client:
        yield client


def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {"message": "Bienvenido a la API"}


def test_post_data(client):
    response = client.post('/data', json={"name": "Test"})
    assert response.status_code == 201
    assert response.json["message"] == "Dato insertado correctamente"


def test_get_all_data(client):
    # Insertar dato primero
    client.post('/data', json={"name": "TestGet"})
    # Obtener todos los datos
    response = client.get('/data')
    assert response.status_code == 200
    assert isinstance(response.json, list)
    assert any(d["name"] == "TestGet" for d in response.json)


def test_post_duplicate_data(client):
    client.post('/data', json={"name": "Duplicado"})
    response = client.post('/data', json={"name": "Duplicado"})
    assert response.status_code == 409
    assert response.json["message"] == "El dato ya existe"


def test_post_without_name(client):
    response = client.post('/data', json={})
    assert response.status_code == 400
    assert response.json["message"] == "El campo 'name' es obligatorio"


def test_delete_existing_data(client):
    # Insertar dato
    client.post('/data', json={"name": "Eliminar"})
    # Obtener ID desde el listado
    get_resp = client.get('/data')
    assert get_resp.status_code == 200
    inserted_id = get_resp.json[0]['id']
    # Eliminar
    delete_resp = client.delete(f'/data/{inserted_id}')
    assert delete_resp.status_code == 200
    assert delete_resp.json["message"] == "Dato eliminado correctamente"


def test_delete_nonexistent_data(client):
    response = client.delete('/data/999')
    assert response.status_code == 404
    assert response.json["message"] == "Dato no encontrado"
