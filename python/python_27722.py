# python - Flask test_client() doesn't have request.authorization with pytest
def test_index(test_client):
    res = test_client.get("/", headers={"Authorization": "Basic {user}".format(user=b64encode(b"test_user:test_password"))})
    assert res.status_code == 200
