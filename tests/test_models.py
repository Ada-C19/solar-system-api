from app.models.planet import Planet
import pytest

def test_to_dict_no_missing_data():
    # Arrange
    test_data = Planet(id = 2,
                    name="Arrakis",
                    description="Spicy",
                    position="#82")

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] == 2
    assert result["name"] == "Arrakis"
    assert result["description"] == "Spicy"
    assert result["position"] == "#82"

def test_to_dict_missing_id():
    # Arrange
    test_data = Planet(name="Arrakis",
                    description="Spicy",
                    position="#82")

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] is None
    assert result["name"] == "Arrakis"
    assert result["description"] == "Spicy"
    assert result["position"] == "#82"

def test_to_dict_missing_name():
    # Arrange
    test_data = Planet(id=1,
                    description="Spicy",
                    position="#82")

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] is None
    assert result["description"] == "Spicy"
    assert result["position"] == "#82"

def test_to_dict_missing_description():
    # Arrange
    test_data = Planet(id = 1,
                    name="Arrakis")

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] == "Arrakis"
    assert result["description"] is None
    assert result["position"] == None


# new tests for from_dict
def test_from_dict_returns_planet():
    # Arrange
    planet_data = {
        "name": "New Planet",
        "description": "The mild planet",
        "position": "#91"
    }

    # Act
    new_planet = Planet.from_dict(planet_data)

    # Assert
    assert new_planet.name == "New Planet"
    assert new_planet.description == "The mild planet"
    assert new_planet.position == "#91"

def test_from_dict_with_no_name():
    # Arrange
    planet_data = {
        "description": "The mild planet"
    }

    # Act & Assert
    with pytest.raises(KeyError, match = 'name'):
        new_planet = Planet.from_dict(planet_data)

def test_from_dict_with_no_description():
    # Arrange
    planet_data = {
        "name": "New planet"
    }

    # Act & Assert
    with pytest.raises(KeyError, match = 'description'):
        new_planet = Planet.from_dict(planet_data)

def test_from_dict_with_extra_keys():
    # Arrange
    planet_data = {
        "extra": "some stuff",
        "name": "New planet",
        "description": "The mild planet",
        "position": "#40"
    }
    
    # Act
    new_planet = Planet.from_dict(planet_data)

    # Assert
    assert new_planet.name == "New planet"
    assert new_planet.description == "The mild planet"
    assert new_planet.position == "#40"