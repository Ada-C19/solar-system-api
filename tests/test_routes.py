# TEST GET ALL PLANETS
def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

# TEST ONE PLANET
def test_get_one_planet(client, two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Blueto",
        "description": "Watr 4evr",
        "position": "#100"
    }

# TEST CREATE ONE PLANET
def test_create_one_planet(client):
    # Act
    response = client.post("/planets", json={
        "name": "Pink Star",
        "description": "Surface made of pink glitter",
        "position": "#68"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == "Planet Pink Star successfully created"


