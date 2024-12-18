import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    return app.test_client()

def test_login(client):
    response = client.post('/api/login', json={'username': 'test', 'password': 'password'})
    assert response.status_code == 200
    assert 'token' in response.json
