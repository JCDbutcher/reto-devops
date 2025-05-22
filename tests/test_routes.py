import pytest
from app import create_app

@pytest.fixture
def client():
    # Usamos el entorno 'testing' que utiliza una DB en memoria
    app = create_app('testing')
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_data(client):
    response = client.get('/data')
    assert response.status_code == 200
