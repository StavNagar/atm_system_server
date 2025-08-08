def test_deposit_and_balance(client, auth_headers):
    headers = auth_headers("acc1", "pass1")

    res = client.post("/accounts/acc1/deposit", json={"amount": 100}, headers=headers)
    assert res.status_code == 200
    assert res.get_json()["new_balance"] == 100

    res = client.get("/accounts/acc1/balance", headers=headers)
    assert res.status_code == 200
    assert res.get_json()["balance"] == 100

def test_withdraw_success(client, auth_headers):
    headers = auth_headers("acc2", "pass2")

    client.post("/accounts/acc2/deposit", json={"amount": 200}, headers=headers)
    res = client.post("/accounts/acc2/withdraw", json={"amount": 50}, headers=headers)
    assert res.status_code == 200
    assert res.get_json()["new_balance"] == 150

def test_withdraw_insufficient_funds(client, auth_headers):
    headers = auth_headers("acc3", "pass3")

    client.post("/accounts/acc3/deposit", json={"amount": 30}, headers=headers)
    res = client.post("/accounts/acc3/withdraw", json={"amount": 100}, headers=headers)
    assert res.status_code == 400
    assert "Insufficient funds" in res.get_json()["error"]

def test_invalid_deposit_amount(client, auth_headers):
    headers = auth_headers("acc4", "pass4")

    res = client.post("/accounts/acc4/deposit", json={"amount": 0}, headers=headers)
    assert res.status_code == 400

def test_invalid_withdraw_amount(client, auth_headers):
    headers = auth_headers("acc5", "pass5")

    res = client.post("/accounts/acc5/withdraw", json={"amount": -10}, headers=headers)
    assert res.status_code == 400
