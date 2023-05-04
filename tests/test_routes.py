import pytest

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


def test_get_all_planets_with_three_records(client, two_saved_planets):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 2
    assert response_body[0] == {
        "id": 1,
        "name": "Blueto",
        "description": "Watr 4evr",
        "position": "#100"
    }
    assert response_body[1] == {
        "id": 2,
        "name": "Purpley",
        "description": "Ice 4evr",
        "position": "#70"
    }

def test_get_all_planets_with_name_query_matching_none(client, two_saved_planets):
    # Act
    data = {'name': 'Pluto'}
    response = client.get("/planets", query_string = data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_all_planets_with_name_query_matching_one(client, two_saved_planets):
    # Act
    data = {'name': 'Blueto'}
    response = client.get("/planets", query_string = data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 1
    assert response_body[0] == {
        "id": 1,
        "name": "Blueto",
        "description": "Watr 4evr",
        "position": "#100"
    }

def test_get_one_planet_id_not_found(client, two_saved_planets):
    # Act
    response = client.get("/planets/10")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message":"Planet 10 not found"}

def test_get_one_planet_id_invalid(client, two_saved_planets):
    # Act
    response = client.get("/planets/pluto")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {"message":"Planet pluto invalid"}


# new test cases for create_planet

def test_create_one_planet_no_name(client):
    # Arrange
    test_data = {"description": "The mild planet"}

    # Act & Assert
    with pytest.raises(KeyError, match='name'):
        response = client.post("/planets", json=test_data)

def test_create_one_planet_no_description(client):
    # Arrange
    test_data = {"name": "New planet"}

    # Act & Assert
    with pytest.raises(KeyError, match = 'description'):
        response = client.post("/planets", json=test_data)

def test_create_one_planet_with_extra_keys(client, two_saved_planets):
    # Arrange
    test_data = {
        "extra": "some stuff",
        "name": "New planet",
        "description": "The mild planet",
        "position": "#87",
    }

    # Act
    response = client.post("/planets", json=test_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == "Planet New planet successfully created"