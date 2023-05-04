import pytest

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
        "name": "Mercury Planet",
        "description": "Smallest planet in the solar system. Its year is 88 days long. Closest to the Sun",
        "type": "Rocky/Terrestrial"
    }


def test_create_one_planet(client):
    # Act
    response = client.post("/planets", json={
        "name": "New Planet",
        "description": "The Best Planet!",
        "type": "Various types"
    })

    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == "Planet New Planet successfully created"


def test_get_all_planets_with_two_records(client, two_saved_planets):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 2
    assert response_body[0] == {
        "id": 1,
        "name": "Mercury Planet",
        "description": "Smallest planet in the solar system. Its year is 88 days long. Closest to the Sun",
        "type": "Rocky/Terrestrial"
    }
    assert response_body[1] == {
        "id": 2,
        "name": "Venus Planet",
        "description": "Hottest planet in the solar system. Has a thick, toxic atmosphere. Second planet from the Sun",
        "type": "Rocky/Terrestrial"
    }

# When we have records and a `name` query in the request arguments, `get_all_planets` returns a list containing only the planet(s) which match the query
def test_get_all_planets_with_name_query_matching_none(client, two_saved_planets):
    # Act
    data = {'name': 'Mercury'}
    response = client.get("/planets", query_string = data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

# When we have records and a `name` query in the request arguments, `get_all_planets` returns a list containing only the planets which match the query
def test_get_all_planets_with_name_query_matching_one(client, two_saved_planets):
    # Act
    data = {'name': 'Mercury'}
    response = client.get("/planets", query_string=data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 0
    assert response_body == []
        # "id": 1,
        # "name": "Mercury",
        # "description": "Smallest planet in the solar system. Its year is 88 days long. Closest to the Sun"
        # "type": "Rocky/Terrestrial"

# When we call `read_one_planet` with a numeric ID that doesn't have a record, we get the expected error message
def test_get_one_planet_id_not_found(client, two_saved_planets):
    # Act
    response = client.get("/planets/10")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message":"planet 10 not found"}

# When we call `read_one_planet` with a non-numeric ID, we get the expected error message
def test_get_one_planet_id_invalid(client, two_saved_planets):
    # Act
    response = client.get("/planets/Pluto")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {"message":"planet Pluto invalid"}

def test_create_one_planet_no_name(client):
    # Arrange
    test_data = {"description": "The Best!",
                "type": "Gas Giant"}

    # Act & Assert
    with pytest.raises(KeyError, match='name'):
        response = client.post("/planets", json=test_data)

def test_create_one_planet_no_description(client):
    # Arrange
    test_data = {"name": "Pluto",
                "type": "Ice Giant"}

    # Act & Assert
    with pytest.raises(KeyError, match = 'description'):
        response = client.post("/planets", json=test_data)

def test_create_one_planet_with_extra_keys(client, two_saved_planets):
    # Arrange
    test_data = {
        "extra": "some stuff",
        "name": "Pluto",
        "description": "The Best!",
        "type": "Gas Giant",
        "another": "last value"
    }

    # Act
    response = client.post("/planets", json=test_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == "Planet Pluto successfully created"