from app.models.planet import Planet


def test_get_all_planets_returns_empty_list_when_db_is_empty(client):
    #act
    response = client.get("/planets")

    #assert
    assert response.status_code == 200
    assert response.get_json() == []

def test_get_one_planet_by_id(client, multiple_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "description": "A dusty, cold, desert world with a very thin atmosphere",
        "gravity": "3.721 m/s²",
        "habitable": False,
        "id": 1,
        "moon_of_planet": "Phobos & Deimos",
        "name": "Mars",
        "nickname": "Red Planet",
        "size": "6,792 km"
    }

def test_get_one_planet_with_no_data(client):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message": "Planet 1 not found"}

def test_get_one_planet_with_id_not_found(client, multiple_planets):
    # Act
    response = client.get("/planets/5")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message": "Planet 5 not found"}

def test_get_list_of_all_planets(client, multiple_planets):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [{
        "description": "A dusty, cold, desert world with a very thin atmosphere",
        "gravity": "3.721 m/s²",
        "habitable": False,
        "id": 1,
        "moon_of_planet": "Phobos & Deimos",
        "name": "Mars",
        "nickname": "Red Planet",
        "size": "6,792 km"
    }, {
        "name": "Saturn",
        "description": "The second-largest planet in solar system.",
        "size": "36,183.7 miles",
        "moon_of_planet": "Iapetus, Rhea, Dione, and Tethys",
        "habitable": False,
        "id": 2,
        "gravity": "10.44 m/s²",
        "nickname": "Ringed Planet"
    }, {
        "name": "Neptune",
        "description": "Dark, cold, and whipped by supersonic winds, ice giant.",
        "size": "24,622 km",
        "moon_of_planet": "Triton",
        "habitable": False,
        "id": 3,
        "gravity": "11.15 m/s²",
        "nickname": "Ice Giant"
    }]

def test_creates_one_planet(client):
    #Arrange
    Expected_planet = {
    "name": "Venus",
    "description": "It is the brightest object in the skynafter the Sun and the Moon",
    "size": "12,104km",
    "moon_of_planet": None,
    "habitable": False,
    "gravity": "8.87 m/s²",
    "nickname": "Morning Star, Evening Star"
}

    # Act
    response = client.post("/planets", json=Expected_planet)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == "Planet Venus successfully created"


def test_replace_planet_returns_seeded_planet(client, multiple_planets):
    replaced_planet = {
    "name": "Earth",
    "description": "A rocky, terrestrial planet.",
    "size": "12,756 km",
    "parent_planet": None,
    "moon_of_planet": "The moon", 
    "habitable": True,
    "gravity": "9.807 m/s²",
    "nickname": "Blue Planet, Gaia, Terra"
}
    response=client.put("/planets/1", json= replaced_planet) 
    actual_planet = Planet.query.get(1) 
    response_body = response.get_json()
    assert response.status_code == 200
    assert response_body == "Planet Earth updated"
    assert actual_planet.name == replaced_planet["name"]

def test_delete_planet(client, multiple_planets):
    # Act
    response = client.delete("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == "Planet Mars successfully deleted"


