from app.models.planet import Planet
import pytest

def test_to_dict_no_missing_data():
    # Arrange
    test_data = Planet(id = 1,
                    name="Mercury",
                    description="Smallest planet in the solar system. Its year is 88 days long. Closest to the Sun.",
                    type="Rocky/Terrestrial")

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] == "Mercury"
    assert result["description"] == "Smallest planet in the solar system. Its year is 88 days long. Closest to the Sun."
    assert result["type"] == "Rocky/Terrestrial"

def test_to_dict_missing_id():
    # Arrange
    test_data = Planet(name="Mercury",
                    description="Smallest planet in the solar system. Its year is 88 days long. Closest to the Sun.",
                    type="Rocky/Terrestrial")
    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] is None
    assert result["name"] == "Mercury"
    assert result["description"] == "Smallest planet in the solar system. Its year is 88 days long. Closest to the Sun."
    assert result["type"] == "Rocky/Terrestrial"

def test_to_dict_missing_name():
    # Arrange
    test_data = Planet(id=1,
                    description="Smallest planet in the solar system. Its year is 88 days long. Closest to the Sun.",
                    type="Rocky/Terrestrial")

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] is None
    assert result["description"] == "Smallest planet in the solar system. Its year is 88 days long. Closest to the Sun."
    assert result["type"] == "Rocky/Terrestrial"

def test_to_dict_missing_description():
    # Arrange
    test_data = Planet(id = 1,
                    name="Mercury",
                    type="Rocky/Terrestrial")

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] == "Mercury"
    assert result["description"] is None
    assert result["type"] == "Rocky/Terrestrial"

def test_to_dict_missing_type():
    # Arrange
    test_data = Planet(id = 1,
                    name="Mercury",
                    description="Smallest planet in the solar system. Its year is 88 days long. Closest to the Sun.")

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] == "Mercury"
    assert result["description"] == "Smallest planet in the solar system. Its year is 88 days long. Closest to the Sun."
    assert result["type"] is None

def test_from_dict_returns_planet():
    # Arrange
    planet_data = {
        "name": "Pluto",
        "description": "The Best!",
        "type": "Ice Giant"
    }

    # Act
    new_planet = Planet.from_dict(planet_data)

    # Assert
    assert new_planet.name == "Pluto"
    assert new_planet.description == "The Best!"

def test_from_dict_with_no_name():
    # Arrange
    planet_data = {
        "description": "The Best!",
        "type": "Ice Giant"
    }

    # Act & Assert
    with pytest.raises(KeyError, match = 'name'):
        new_planet = Planet.from_dict(planet_data)

def test_from_dict_with_no_description():
    # Arrange
    planet_data = {
        "name": "Pluto",
        "type": "Ice Giant"
    }

    # Act & Assert
    with pytest.raises(KeyError, match = 'description'):
        new_planet = Planet.from_dict(planet_data)

def test_from_dict_with_no_type():
    # Arrange
    planet_data = {
        "name": "Pluto",
        "description": "The Best!"
    }

    # Act & Assert
    with pytest.raises(KeyError, match = 'type'):
        new_planet = Planet.from_dict(planet_data)

def test_from_dict_with_extra_keys():
    # Arrange
    planet_data = {
        "extra": "some stuff",
        "name": "Pluto",
        "description": "The Best!",
        "type": "Ice Giant",
        "another": "last value"
    }
    
    # Act
    new_planet = Planet.from_dict(planet_data)

    # Assert
    assert new_planet.name == "Pluto"
    assert new_planet.description == "The Best!"
    assert new_planet.type == "Ice Giant"
