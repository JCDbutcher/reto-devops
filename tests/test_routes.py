import pytest
from app import create_app, db

@pytest.fixture
def client():
    # Crea la app con configuración de test
    app = create_app('testing')
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # DB temporal en memoria

    with app.app_context():
        db.create_all()  # ✅ Crea las tablas

    # Devuelve el cliente de pruebas
    with app.test_client() as client:
        yield client

def test_get_data(client):
    response = client.get('/data')
    assert response.status_code == 200
