def test_get_all_planets_with_no_records(client):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet(client, two_planets):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Planet1",
        "description": "First planet",
        "diameter": 5000
    }

def test_get_planet_with_nonexistent_id_returns_404(client):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {"message":"Planet 1 not found"}

def test_get_all_planets_with_data(client, two_planets):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body[0] == {
        "id": 1,
        "name": "Planet1",
        "description": "First planet",
        "diameter": 5000
    }
    assert response_body[1] == {
        "id": 2,
        "name": "Planet2",
        "description": "Second planet",
        "diameter": 7500
    }

def test_add_one_planet_to_empty_db(client):
    response = client.post("/planets", json={
        "name": "Planet1",
        "description": "First planet",
        "diameter": 5000
    })

    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == "Planet Planet1 successfully created"