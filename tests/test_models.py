from app.models.planet import Planet
import pytest

# Tests for to_dict
def test_to_dict_no_missing_data():
    # Arrange

    test_data = Planet(id = 1,
            name = "Venus",
            description = "hot enough to melt lead n ur heart </3",
            color = "she lil' rusty :(")
    
    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] == "Venus"
    assert result["description"] == "hot enough to melt lead n ur heart </3"
    
    

def test_to_dict_missing_id():
    # Arrange
    test_data = Planet(
            name = "Venus",
            description = "hot enough to melt lead n ur heart </3",
            color = "she lil' rusty :(")

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] is None
    assert result["name"] == "Venus"
    assert result["description"] == "hot enough to melt lead n ur heart </3"
    assert result["color"] == "she lil' rusty :("


def test_to_dict_missing_name():
    #Arrange
    test_data = Planet(id=1,
                description="hot enough to melt lead n ur heart </3",
                color="she lil' rusty :(")
    #Act
    result = test_data.to_dict()

    #Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] is None
    assert result["description"] == "hot enough to melt lead n ur heart </3"
    assert result["color"] == "she lil' rusty :("


def test_to_dict_missing_description():
    #Arrange
    test_data = Planet(id=1,
                name="Venus",
                color="she lil' rusty :(")
    
    #Act
    result = test_data.to_dict()

    #Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] == "Venus"
    assert result["description"] is None
    assert result["color"] == "she lil' rusty :("


# Tests for from_dict
def test_from_dict_returns_planet():
    planet_data = {"name": "Earth",
                "description":"loud",
                "color":"blue & green"}
    # Act & Assert
    new_planet = Planet.from_dict(planet_data)

    assert new_planet.name == "Earth"
    assert new_planet.description == "loud"
    assert new_planet.color == "blue & green"


def test_from_dict_with_no_description():
    # Arrange
    planet_data = {"name": "Earth",
                 "color": "blue & green"}

    # Act & Assert
    with pytest.raises(KeyError, match = "description"):
        new_planet = Planet.from_dict(planet_data)

def test_from_dict_with_extra_keys():
    # Arrange
    planet_data = {
        "name": "New Planet",
        "description": "pretty",
        "color": "pink",
        "habitable?": "yes, let's move!!"
    }

    # Act
    new_planet = Planet.from_dict(planet_data)

    # Assert
    assert new_planet.name == "New Planet"
    assert new_planet.description == "pretty"
    assert new_planet.color == "pink"
    