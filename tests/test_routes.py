#from werkzeug.exceptions import HTTPException
# from app.routes import validate_book
import pytest

def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_first_planet(client, two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "first planet",
        "description": "the first one",
        "composition": "first"
    }

def test_get_first_planet_from_empty_database(client):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {'message': 'Planet with id 1 was not found'}

def test_get_all_planets(client, two_saved_planets):
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [
        {"id": 1,
        "name": "first planet",
        "description": "the first one",
        "composition": "first"},
        {"id": 2,
        "name": "second planet",
        "description": "the second one",
        "composition": "second"}
    ]

def test_post_one_planet_returns_201(client):
    # Act
    response = client.post("/planets", json={
        "name": "new planet",
        "description": "the new one",
        "composition": "new"
    })
    response_body = response.get_data(as_text=True)

    # Assert
    assert response.status_code == 201
    assert response_body == "Planet new planet successfully created"