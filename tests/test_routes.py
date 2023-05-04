from app.models.planet import Planet

def test_get_all_returns_empty_list_when_database_is_empty(client):

    #Act
    response = client.get("/planets")

    #Assert
    assert response.status_code == 200
    assert response.get_json() == []


def test_get_one_planet_returns_seeded_planet(client, one_planet):

    #Act
    response = client.get(f"/planets/{one_planet.id}")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert response_body["id"] == one_planet.id
    assert response_body["name"] == one_planet.name
    assert response_body["description"] == one_planet.description
    assert response_body["mass"] == one_planet.mass


def test_create_planet_happy_path(client):

    #Arrange
    EXPECTED_PLANET = {
        "name": "test_name",
        "description": "test_description",
        "mass": "mass"}

    #Assert
    response = client.post("/planets", json=EXPECTED_PLANET)
    response_body = response.get_data(as_text=True)

    actual_planet = Planet.query.get(1)
    assert response.status_code == 201
    assert response_body == f"Planets {EXPECTED_PLANET["name"]} successfully created"
    assert actual_planet.name == EXPECTED_PLANET["name"]
    assert actual_planet.description == EXPECTED_PLANET["description"]
    assert actual_planet.mass == EXPECTED_PLANET["mass"]


