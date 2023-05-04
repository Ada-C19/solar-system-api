import pytest
from werkzeug.exceptions import HTTPException
from app.routes import validate_model
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
        "name": "Mercury Planet",
        "description": "Smallest planet in the solar system. Its year is 88 days long. Closest to the Sun",
        "type": "Rocky/Terrestrial"
    }


def test_create_one_planet(client):
    # Act
    response = client.post("/planets", json={
        "name": "Pluto",
        "description": "The Best Planet!",
        "type": "Various types"
    })

    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == "Planet Pluto successfully created"


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
    assert response_body == {"message":"Planet 10 not found"}

# When we call `read_one_planet` with a non-numeric ID, we get the expected error message
def test_get_one_planet_id_invalid(client, two_saved_planets):
    # Act
    response = client.get("/planets/Pluto")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {"message":"Planet Pluto invalid"}

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

def test_update_planet(client, two_saved_planets):
    # Arrange
    test_data = {
        "name": "Pluto",
        "description": "The Best!",
        "type": "Ice Giant",
    }

    # Act
    response = client.put("/planets/1", json=test_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == "Planet #1 successfully updated"

def test_update_planet_with_extra_keys(client, two_saved_planets):
    # Arrange
    test_data = {
        "extra": "some stuff",
        "name": "Pluto",
        "description": "The Best!",
        "type": "Ice Giant",
        "another": "last value"
    }

    # Act
    response = client.put("/planets/1", json=test_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == "Planet #1 successfully updated"

def test_update_planet_missing_record(client, two_saved_planets):
    # Arrange
    test_data = {
        "name": "Pluto",
        "description": "The Best!"
    }

    # Act
    response = client.put("/planets/3", json=test_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message": "Planet 3 not found"}

def test_update_planet_invalid_id(client, two_saved_planets):
    # Arrange
    test_data = {
        "name": "cat",
        "description": "The Best!",
        "type": "Ice Giant"
    }

    # Act
    response = client.put("/planets/cat", json=test_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {"message": "Planet cat invalid"}

def test_delete_planet(client, two_saved_planets):
    # Act
    response = client.delete("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == "Planet #1 successfully deleted"

def test_delete_planet_missing_record(client, two_saved_planets):
    # Act
    response = client.delete("/planets/3")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message": "Planet 3 not found"}

def test_delete_planet_invalid_id(client, two_saved_planets):
    # Act
    response = client.delete("/planets/cat")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {"message": "Planet cat invalid"}

def test_validate_model(two_saved_planets):
    # Act
    result_planet = validate_model(Planet, 1)

    # Assert
    assert result_planet.id == 1
    assert result_planet.name == "Mercury Planet"
    assert result_planet.description == "Smallest planet in the solar system. Its year is 88 days long. Closest to the Sun"
    assert result_planet.type == "Rocky/Terrestrial"

def test_validate_model_missing_record(client, two_saved_planets):
    # Act & Assert
    # Calling `validate_planet` without being invoked by a route will
    # cause an `HTTPException` when an `abort` statement is reached 
    with pytest.raises(HTTPException):
        result_planet = validate_model(Planet, "3")
    
def test_validate_model_invalid_id(two_saved_planets):
    # Act & Assert
    # Calling `validate_planet` without being invoked by a route will
    # cause an `HTTPException` when an `abort` statement is reached 
    with pytest.raises(HTTPException):
        result_planet = validate_model(Planet, "cat")
