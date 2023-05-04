import pytest
from app.routes import validate_model
from werkzeug.exceptions import HTTPException
from app.models.planet import Planet

#Tests our validate_model Helper Function:
def test_validate_model(two_saved_planets):
    # Act
    result_planet = validate_model(Planet, 1)

    # Assert
    assert result_planet.id == 1
    assert result_planet.name== "Venus"
    assert result_planet.description == "hot enough to melt lead n ur heart </3"
    assert result_planet.color == "she lil' rusty :("

def test_validate_model_missing_record(two_saved_planets):
    
    # Act & Assert
    with pytest.raises(HTTPException):
        result_planet = validate_model(Planet, "3")
    
def test_validate_model_invalid_id(two_saved_planets):
    # Act & Assert
    with pytest.raises(HTTPException):
        result_planet = validate_model(Planet, "cat")


#Tests our endpoints
def test_get_all_planets_empty_200(client):
    # Act
    response = client.get("/planets")

    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

# `GET` `/planets/1` returns a response body that matches our fixture

def test_get_one_planet(client, two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    
    assert response_body == {
            "id": 1,
            "name": "Venus",
            "description": "hot enough to melt lead n ur heart </3",
            "color": "she lil' rusty :("
        }


# `GET` `/planets/1` with no data in test database (no fixture) returns a `404`

def test_get_one_planet_empty_404_status_code(client):
    # Act
    response = client.get("/planets/1")

    # Assert
    assert response.status_code == 404
    
# `GET` `/planets` with valid test data (fixtures) returns a `200` with an array including appropriate test data
def test_get_all_planets(client, two_saved_planets):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()


    # Assert
    assert response.status_code == 200
    assert response_body == [
            {"id": 1,
            "name": "Venus",
            "description": "hot enough to melt lead n ur heart </3",
            "color": "she lil' rusty :("},
            {"id": 2,
            "name": "Saturn",
            "description": "bling bling rings",
            "color": "she cute pink :("}
    ]
    
# `POST` `/planets` with a JSON request body returns a `201`

def test_create_one_book(client):
    # Act
    response = client.post("/planets", json={
        "name": "New Planet",
        "description": "is this.. the new Earth?",
        "color": "pink"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    def test_create_one_planet_no_name(client):
        test_data = {"description":"loud",
        "color":"blue & green"}
    # Act & Assert
        with pytest.raises(KeyError, match='name'):
            response = client.post("/planets", json=test_data)

def test_create_one_planet_no_description(client):
    # Arrange
    test_data = {"name": "Earth",
                "color": "blue & green"}

    # Act & Assert
    with pytest.raises(KeyError, match = "description"):
        response = client.post("/planets", json=test_data)

def test_create_one_planet_with_extra_keys(client):
    # Arrange
    test_data = {
        "name": "New Planet",
        "description": "pretty",
        "color": "pink",
        "habitable?": "yes, let's move!!"
    }

    # Act
    response = client.post("/planets", json=test_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    