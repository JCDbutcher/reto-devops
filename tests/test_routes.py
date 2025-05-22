from app import create_app
import pytest

@pytest.fixture
def client():
    app = create_app('development')
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_data(client):
    response = client.get('/data')
    assert response.status_code == 200
