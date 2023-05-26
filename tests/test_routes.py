import pytest

def test_post_creates_planet(client):
    response = client.post("/planet", json={
        "name": "earth",
        "description": "in danger",
        "num_moons": 1
    })

    response_body = response.get_json()

    assert response.status_code == 201
    assert "id" in response_body

def test_get_all_planets(client, two_planets):
    response = client.get("/planet")

    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == [
        {
            "id": 1,
            "name": "earth",
            "description": "in danger",
            "num_moons": 1
        },
        {
            "id": 2,
            "name": "mars",
            "description": "red",
            "num_moons": 2
        }
    ]

def test_get_one_planet(client, two_planets):
    response = client.get("/planet/1")

    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "earth",
        "description": "in danger",
        "num_moons": 1
    }

def test_put_planet(client, two_planets):
    response = client.put("/planet/1", json = {
        "id": 1,
        "name": "mercury",
        "description": "small",
        "num_moons": 0

    })

    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {"msg": "planet 1 successfully updated"}

def test_delete_planet(client, two_planets):
    response = client.delete("/planet/2")

    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {"msg": "planet 2 successfully deleted"}

def test_get_no_data_returns_404(client):
    response = client.get("/planet/20")

    response_body = response.get_json()

    assert response.status_code == 404


