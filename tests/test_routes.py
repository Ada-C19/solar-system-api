import pytest

def test_get_all_planets(client, two_planets):
    response = client.get("/planet")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == [{
        "id": 1,
        "name": "Saturn",
        "description": "the ringed planet",
        "size": 72367
    }, 
    {
        "id": 2,
        "name": "Uranus",
        "description": "seventh planet from the Sun",
        "size": 31518
    }]

def test_get_one_planet(client, two_planets):
    response = client.get("/planet/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Saturn",
        "description": "the ringed planet",
        "size": 72367
    }

def test_get_one_planet_empty_dataset(client):
    response = client.get("/planet/1")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body is None

def test_post_creates_planet(client):
    response = client.post("/planet", json={
        "name": "Saturn",
        "description": "the ringed planet",
        "size": 72367
    })

    response_body = response.get_json()

    assert response.status_code == 201
    assert "id" in response_body

def test_put_planet(client, two_planets):
    response = client.put("/planet/1", json={
        "name": "Earth",
        "description": "the blue planet",
        "size": 7917
    })
    response_body = response.get_json()

    assert response.status_code == 200
    assert "Planet 1 successfully updated" in response_body["msg"]

def test_delete_planet(client, two_planets):
    response = client.delete("/planet/2")
    response_body = response.get_json()

    assert response.status_code == 200
    assert "Planet 2 successfully deleted" in response_body["msg"]