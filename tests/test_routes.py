from werkzeug.exceptions import HTTPException
from app.models.planet import Planet
from app.routes import validate_model
import pytest

# test returns empty array and 200 by retrieving all planets
def test_get_all_planets_with_no_records(client):
	# Act
    response = client.get("/planets")
    response_body = response.get_json()
 	
 	# Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet_returns_seeded_planet(client, one_planet):
    # Act
    response = client.get(f"/planets/{one_planet.id}")
    response_body = response.get_json()
 	
 	# Assert
    assert response.status_code == 200
    assert response_body["name"] == one_planet.name
    assert response_body["description"] == one_planet.description
    assert response_body["color"] == one_planet.color

def test_get_planet_not_found(client):
    # Act
    response = client.get('/planets/1')

    # Assert
    assert response.status_code == 404

def test_get_all_planets_returns_seeded_planets(client, get_all_planets):
 	# Act
    response = client.get(f"/planets")
    response_body = response.get_json()
 	
 	# Assert 
    assert response.status_code == 200
    assert len(response_body) == 2
    assert response_body[0] == {
        "id" : 1,
        "name" : "Venus",
        "description" : "Planet of love",
        "color" : "orange"
    }
    assert response_body[1] == {
        "id" : 2,
        "name" : "Earth",
        "description" : "Home",
        "color" : "blue-green"
    }

def test_create_planet_happy_path(client):
    EXPECTED_PLANET = dict(
        name = "Mars", 
        description = "Planet of War", 
        color = "Red"
    )
        
    # Act 
    response = client.post("/planets", json=EXPECTED_PLANET)
    response_body = response.get_data(as_text = True)
    
    actual_planet = Planet.query.get(1)
 	
 	# Assert
    assert response.status_code == 201
    assert response_body == f"Planet {EXPECTED_PLANET['name']} sucessfully created"
 	
    assert EXPECTED_PLANET["name"] == actual_planet.name
    assert EXPECTED_PLANET["description"] == actual_planet.description
    assert EXPECTED_PLANET["color"] == actual_planet.color

# tests for make_planet_dict

def test_to_dict_no_missing_data():
    # Arrange
    test_data = Planet(
                    id = 1,
                    name = "Mars",
                    description = "Planet of War",
                    color = "Red"
                    )

    # Act
    result = test_data.make_planet_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] == "Mars"
    assert result["description"] == "Planet of War"
    assert result["color"] == "Red"


def test_to_dict_missing_id():
    # Arrange
    test_data = Planet(
                    name = "Mars",
                    description = "Planet of War",
                    color = "Red"
                    )

    # Act
    result = test_data.make_planet_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] is None
    assert result["name"] == "Mars"
    assert result["description"] == "Planet of War"
    assert result["color"] == "Red"

def test_to_dict_missing_name():
    # Arrange
    test_data = Planet(
                    id = 1,
                    description = "Planet of War",
                    color = "Red"
                    )

    # Act
    result = test_data.make_planet_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] is None
    assert result["description"] == "Planet of War"
    assert result["color"] == "Red"

def test_to_dict_missing_description():
    # Arrange
    test_data = Planet(
                    id = 1,
                    name = "Mars",
                    color = "Red"
                    )

    # Act
    result = test_data.make_planet_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] == "Mars"
    assert result["description"] is None
    assert result["color"] == "Red"

# tests for for_dict

def test_from_dict_returns_planet():
    # Arrange
    planet_data = {
        "name": "Mars",
        "description": "Planet of War",
        "color" : "Red"
    }

    # Act
    new_planet = Planet.from_dict(planet_data)

    # Assert
    assert new_planet.name == "Mars"
    assert new_planet.description == "Planet of War"
    assert new_planet.color == "Red"

def test_from_dict_with_no_name():
    # Arrange
    planet_data = {
        "description": "Planet of War",
        "color" : "Red"
    }

    # Act & Assert
    with pytest.raises(KeyError, match = 'name'):
        Planet.from_dict(planet_data)

def test_from_dict_with_no_description():
    # Arrange
    planet_data = {
        "name": "Mars",
        "color" : "Red"
    }

    # Act & Assert
    with pytest.raises(KeyError, match = 'description'):
        Planet.from_dict(planet_data)

# tests for validate_model

def test_validate_model(get_all_planets):
    # Act
    result_planet = validate_model(Planet, 1)
    result_planet_two = validate_model(Planet, 2)

    # Assert for planet 1
    assert result_planet.id == 1
    assert result_planet.name == "Venus"
    assert result_planet.description == "Planet of love"
    assert result_planet.color == "orange"
    
    # Assert for planet 2
    assert result_planet_two.id == 2
    assert result_planet_two.name == "Earth"
    assert result_planet_two.description == "Home"
    assert result_planet_two.color == "blue-green"
    

def test_validate_model_missing_record(get_all_planets):
    # Act & Assert
    # Calling `validate_model` without being invoked by a route will
    # cause an `HTTPException` when an `abort` statement is reached 
    with pytest.raises(HTTPException):
        validate_model(Planet, "3")
    
def test_validate_model_invalid_id(get_all_planets):
    # Act & Assert
    # Calling `validate_model` without being invoked by a route will
    # cause an `HTTPException` when an `abort` statement is reached 
    with pytest.raises(HTTPException):
        validate_model(Planet, "cat")