from app.models.planet import Planet
import pytest


def test_to_dict_no_missing_data():
    test_data = Planet(id=1,
                       name="Mercury",
                       description="The smallest planet; pitted and streaky, brownish-gray",
                       distance_from_the_sun=0.39)

    result = test_data.to_dict()

    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] == "Mercury"
    assert result["description"] == "The smallest planet; pitted and streaky, brownish-gray"
    assert result["distance_from_the_sun"] == 0.39


def test_to_dict_missing_id():
    test_data = Planet(name="Mercury",
                       description="The smallest planet; pitted and streaky, brownish-gray",
                       distance_from_the_sun=0.39)

    result = test_data.to_dict()

    assert len(result) == 4
    assert result["id"] is None
    assert result["name"] == "Mercury"
    assert result["description"] == "The smallest planet; pitted and streaky, brownish-gray"
    assert result["distance_from_the_sun"] == 0.39


def test_to_dict_missing_name():
    test_data = Planet(id=1,
                       description="The smallest planet; pitted and streaky, brownish-gray",
                       distance_from_the_sun=0.39)

    result = test_data.to_dict()

    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] is None
    assert result["description"] == "The smallest planet; pitted and streaky, brownish-gray"
    assert result["distance_from_the_sun"] == 0.39


def test_to_dict_missing_description():
    test_data = Planet(id=1,
                       name="Mercury",
                       distance_from_the_sun=0.39)

    result = test_data.to_dict()

    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] == "Mercury"
    assert result["description"] is None
    assert result["distance_from_the_sun"] == 0.39


def test_to_dict_missing_distance():
    test_data = Planet(id=1,
                       name="Mercury",
                       description="The smallest planet; pitted and streaky, brownish-gray")

    result = test_data.to_dict()

    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] == "Mercury"
    assert result["description"] == "The smallest planet; pitted and streaky, brownish-gray"
    assert result["distance_from_the_sun"] is None


def test_from_dict_returns_planet():
    planet_data = {
        "name": "Saturn",
        "description": "A yellowish gas giant with rings made of ice and rock",
        "distance_from_the_sun": 9.54
    }

    new_planet = Planet.from_dict(planet_data)

    assert new_planet.name == "Saturn"
    assert new_planet.description == "A yellowish gas giant with rings made of ice and rock"
    assert new_planet.distance_from_the_sun == 9.54


def test_from_dict_with_no_name():
    planet_data = {
        "description": "A yellowish gas giant with rings made of ice and rock",
        "distance_from_the_sun": 9.54
    }

    with pytest.raises(KeyError, match="name"):
        new_planet = Planet.from_dict(planet_data)


def test_from_dict_with_no_description():
    planet_data = {
        "name": "Saturn",
        "distance_from_the_sun": 9.54
    }

    with pytest.raises(KeyError, match="description"):
        new_planet = Planet.from_dict(planet_data)


def test_from_dict_with_no_distance():
    planet_data = {
        "name": "Saturn",
        "description": "A yellowish gas giant with rings made of ice and rock",
    }

    with pytest.raises(KeyError, match="distance_from_the_sun"):
        new_planet = Planet.from_dict(planet_data)


def test_from_dict_with_extra_keys():
    planet_data = {
        "surface_area": 16.49,
        "name": "Saturn",
        "description": "A yellowish gas giant with rings made of ice and rock",
        "distance_from_the_sun": 9.54,
        "age": 4.503
    }

    new_planet = Planet.from_dict(planet_data)

    assert new_planet.name == "Saturn"
    assert new_planet.description == "A yellowish gas giant with rings made of ice and rock"
    assert new_planet.distance_from_the_sun == 9.54
