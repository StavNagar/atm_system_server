import pytest
from app import create_app
from flask.testing import FlaskClient

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "JWT_SECRET_KEY": "test-secret",
    })
    yield app

@pytest.fixture
def client(app) -> FlaskClient:
    return app.test_client()

@pytest.fixture
def auth_headers(client):
    def _get_headers(account_number="testuser", password="testpass"):
        client.post("/auth/register", json={
            "account_number": account_number,
            "password": password,
        })
        login_resp = client.post("/auth/login", json={
            "account_number": account_number,
            "password": password,
        })
        token = login_resp.get_json()["access_token"]
        return {"Authorization": f"Bearer {token}"}
    return _get_headers
