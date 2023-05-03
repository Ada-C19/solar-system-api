import pytest
from werkzeug.exceptions import HTTPException
from app.routes import validate_model
from app.models.planet import Planet

def test_get_all_planets_with_no_records(client):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 0
    assert response_body == []


def test_get_all_planets_with_two_records(client, two_saved_planets):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 2
    assert response_body[0] == {
        "id": 1,
        "name": "Mercury",
        "description": "The smallest planet; pitted and streaky, brownish-gray",
        "distance_from_the_sun": 0.39
    }
    assert response_body[1] == {
        "id": 2,
        "name": "Venus",
        "description": "A fireball with temperatures hot enough to melt lead, covered in thick clouds",
        "distance_from_the_sun": 0.72
    }


def test_get_all_planets_with_name_query_matching_none(client, two_saved_planets):
    data = {"name": "Eros"}
    response = client.get("/planets", query_string=data)
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []


def test_get_all_planets_with_name_query_matching_one(client, two_saved_planets):
    data = {"name": "Venus"}
    response = client.get("/planets", query_string=data)
    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 1
    assert response_body[0] == {
        "id": 2,
        "name": "Venus",
        "description": "A fireball with temperatures hot enough to melt lead, covered in thick clouds",
        "distance_from_the_sun": 0.72
    }


def test_get_one_planet(client, two_saved_planets):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Mercury",
        "description": "The smallest planet; pitted and streaky, brownish-gray",
        "distance_from_the_sun": 0.39
    }


def test_get_one_planet_missing_record(client, two_saved_planets):
    response = client.get("/planets/100")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {"message": "Planet 100 not found"}


def test_get_one_planet_invalid_id(client, two_saved_planets):
    response = client.get("planets/faraway")
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == {"message": "Planet faraway invalid"}


def test_create_one_planet(client):
    test_data = {
        "name": "Earth",
        "description": "A beautiful blue-green planet with life-supporting atmosphere",
        "distance_from_the_sun": 1.00
    }
    response = client.post("/planets", json=test_data)
    response_body = response.get_data(as_text=True)

    assert response.status_code == 201
    assert response_body == "Planet Earth successfully created"


def test_create_one_planet_no_name(client):
    test_data = {
        "description": "A beautiful blue-green planet with life-supporting atmosphere",
        "distance_from_the_sun": 1.00
    }

    with pytest.raises(KeyError, match="name"):
        response = client.post("/planets", json=test_data)


def test_create_one_planet_no_description(client):
    test_data = {
        "name": "Earth",
        "distance_from_the_sun": 1.00
    }

    with pytest.raises(KeyError, match="description"):
        response = client.post("/planets", json=test_data)


def test_create_one_planet_no_distance(client):
    test_data = {
        "name": "Earth",
        "description": "A beautiful blue-green planet with life-supporting atmosphere",
    }

    with pytest.raises(KeyError, match="distance_from_the_sun"):
        response = client.post("/planets", json=test_data)


def test_create_one_planet_with_extra_keys(client, two_saved_planets):
    test_data = {
        "surface_area": 196.9,
        "name": "Earth",
        "description": "A beautiful blue-green planet with life-supporting atmosphere",
        "distance_from_the_sun": 1.00,
        "age": 4.543,
    }

    response = client.post("/planets", json=test_data)
    response_body = response.get_data(as_text=True)

    assert response.status_code == 201
    assert response_body == "Planet Earth successfully created"


def test_update_planet(client, two_saved_planets):
    test_data = {
        "name": "Uranus",
        "description": "A blue-green gas giant which also has a ring system",
        "distance_from_the_sun": 19.19
    }

    response = client.put("/planets/1", json=test_data)
    response_body = response.get_data(as_text=True)

    assert response.status_code == 200
    assert response_body == "Planet #1 successfully updated"


def test_update_planet_with_extra_keys(client, two_saved_planets):
    test_data = {
        "surface_area": 3.121,
        "name": "Uranus",
        "description": "A blue-green gas giant which also has a ring system",
        "distance_from_the_sun": 19.19,
        "age": 4.503
    }

    response = client.put("/planets/1", json=test_data)
    response_body = response.get_data(as_text=True)

    assert response.status_code == 200
    assert response_body == "Planet #1 successfully updated"


def test_update_planet_missing_record(client, two_saved_planets):
    test_data = {
        "name": "Uranus",
        "description": "A blue-green gas giant which also has a ring system",
        "distance_from_the_sun": 19.19
    }

    response = client.put("/planets/300", json=test_data)
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {"message": "Planet 300 not found"}


def test_update_planet_invalid_id(client, two_saved_planets):
    test_data = {
        "name": "Uranus",
        "description": "A blue-green gas giant which also has a ring system",
        "distance_from_the_sun": 19.19
    }

    response = client.put("/planets/nearest", json=test_data)
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == {"message": "Planet nearest invalid"}


def test_delete_one_planet(client, two_saved_planets):
    response = client.delete("planets/1")
    response_body = response.get_data(as_text=True)

    assert response.status_code == 200
    assert response_body == "Planet #1 successfully deleted"


def test_delete_missing_planet(client, two_saved_planets):
    response = client.delete("planets/300")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {"message": "Planet 300 not found"}


def test_delete_planet_invalid_id(client, two_saved_planets):
    response = client.delete("planets/nearest")
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == {"message": "Planet nearest invalid"}


def test_validate_model(two_saved_planets):
    result_planet = validate_model(Planet, 1)

    assert result_planet.id == 1
    assert result_planet.name == "Mercury"
    assert result_planet.description == "The smallest planet; pitted and streaky, brownish-gray"
    assert result_planet.distance_from_the_sun == 0.39


def test_validate_model_missing_record(two_saved_planets):
    with pytest.raises(HTTPException):
        result_planet = validate_model(Planet, "300")


def test_validate_model_invalid_id(two_saved_planets):
    with pytest.raises(HTTPException):
        result_planet = validate_model(Planet, "cat")


