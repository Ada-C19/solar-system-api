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