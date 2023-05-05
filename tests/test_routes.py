from app.models.planet import Planet

def test_get_all_planetss_return_empty_list_when_db_is_empty(client):
    # Act
    response = client.get("/planets")

    # Assert
    assert response.status_code == 200
    assert response.get_json() == []

def test_get_one_planet_returns_seeded_planet(client, one_planet):
    # Act
    response = client.get(f"/planets/{one_planet.id}")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body["id"] == one_planet.id
    assert response_body["name"] == one_planet.name
    assert response_body["description"] == one_planet.description
    assert response_body["rating"] == one_planet.rating

def test_create_planet_happy_path(client):
    EXPECTED_PLANET = dict(
        id="id",
        name="name",
        description="description",
        rating="rating"
    )
    # Act
    response = client.post("/planets", json=EXPECTED_PLANET)
    response_body = response.get_data(as_text=True)

    actual_planet = Planet.query.get(1)

    # Assert
    assert response.status_code == 201
    assert response_body == f"Planet {EXPECTED_PLANET['name']} successfully created"

    assert EXPECTED_PLANET["id"] == actual_planet.id
    assert EXPECTED_PLANET["name"] == actual_planet.name
    assert EXPECTED_PLANET["description"] == actual_planet.description
    assert EXPECTED_PLANET["color"] == actual_planet.rating