from flask import jsonify

def test_get_empty_all_planets(client):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []



def test_get_one_planet(client, two_saved_planets):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {"name": "pluto", "description":"not a planet", "moons":79, "id":1}

def test_get_non_existent_planet(client, two_saved_planets):
    response = client.get("/planets/100")
    response_body = response.get_json()

    assert response.status_code == 404

def test_invalid_planet_route(client, two_saved_planets):
    response = client.get("/planets/ADA")
    response_body = response.get_json()

    assert response.status_code == 400

def test_get_all_planets(client, two_saved_planets):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {{"name": "pluto", "description": "not a planet", "moons": 79, "id": 1}, 
                            {"name": "mercury", "description": "is a planet", "moons" : 5, "id": 2}}