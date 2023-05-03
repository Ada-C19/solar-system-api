from app.models.planet import Planet

def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []


def test_get_one_planet(client, two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Mercury",
        "description": "smallest planet",
        "association": "Wednesday"
    }

def test_get_one_planet_by_name(client, two_saved_planets):
    # Act
    response = client.get("/planets?name=Mercury")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body[0]['name'] == "Mercury"

def test_create_one_planet(client):
    # Arrange
    expected_planet = dict(name="Saturn",
                           description="the one with the rings",
                           association="Saturday")

    # Act
    response = client.post("/planets", json=expected_planet)
    response_body = response.get_json()
    actual_planet = Planet.query.get(1)

    # Assert
    assert response.status_code == 201
    assert response_body == f"Planet {expected_planet['name']} successfully created."
    assert expected_planet['name'] == actual_planet.name

