import json

import pytest


@pytest.mark.functional
def test_swagger(test_client):
    response = test_client.get("/template/v0.1/ui/")
    assert response.status_code == 200
    assert b"Swagger" in response.data


@pytest.mark.functional
def test_get_functions(test_client, string):
    data = {"params": {"string": string}}
    response = test_client.post("/template/v0.1/reverse", json=data)
    assert response.status_code == 201
    response = json.loads(response.data.decode())
    assert response["result"]["is_palindrome"] is True
