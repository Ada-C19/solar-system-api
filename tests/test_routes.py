def test_get_one_planet(client, two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Mars",
        "description": "Smallest planet"
    }


def test_get_one_planet_no_data_returns_404(client):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404


def test_get_all_planets(client, two_saved_planets):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [{
        "id": 1,
        "name": "Mars",
        "description": "Smallest planet"
        },
        {
        "id": 2,
        "name": "Jupiter",
        "description": "Largest planet"
        }]
    

def test_create_one_planet(client):
    # Act
    response = client.post("/planets", json={
        "name": "Earth",
        "description": "Water planet"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == "Planet Earth successfully created"