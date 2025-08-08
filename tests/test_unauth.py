def test_access_other_account_balance(client, auth_headers):
    headers = auth_headers("userA", "passA")

    res = client.get("/accounts/userB/balance", headers=headers)
    assert res.status_code == 403

def test_deposit_other_account(client, auth_headers):
    headers = auth_headers("userC", "passC")

    res = client.post("/accounts/userD/deposit", json={"amount": 100}, headers=headers)
    assert res.status_code == 403

def test_withdraw_other_account(client, auth_headers):
    headers = auth_headers("userE", "passE")

    res = client.post("/accounts/userF/withdraw", json={"amount": 50}, headers=headers)
    assert res.status_code == 403
