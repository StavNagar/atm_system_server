def test_register_success(client):
    res = client.post("/auth/register", json={"account_number": "user1", "password": "pass"})
    assert res.status_code == 201
    assert res.get_json()["message"] == "Account created"

def test_register_existing_account(client):
    client.post("/auth/register", json={"account_number": "user2", "password": "pass"})
    res = client.post("/auth/register", json={"account_number": "user2", "password": "pass"})
    assert res.status_code == 400

def test_login_success(client):
    client.post("/auth/register", json={"account_number": "user3", "password": "pass"})
    res = client.post("/auth/login", json={"account_number": "user3", "password": "pass"})
    assert res.status_code == 200
    assert "access_token" in res.get_json()

def test_login_fail_wrong_password(client):
    client.post("/auth/register", json={"account_number": "user4", "password": "pass"})
    res = client.post("/auth/login", json={"account_number": "user4", "password": "wrong"})
    assert res.status_code == 401

def test_login_fail_missing_fields(client):
    res = client.post("/auth/login", json={"account_number": "user5"})
    assert res.status_code == 400
