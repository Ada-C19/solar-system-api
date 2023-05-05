from app.models.planet import Planet

def test_get_all_returns_empty_list_when_database_is_empty(client):
    response = client.get("/planets")

    assert response.status_code == 200
    assert response.get_json() == []


def test_get_one_planet_returns_planet(client, get_planets):
    response = client.get(f"/planets/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {"id" : 1, "name" : "test_name_2", "description" : "test_description_2", "mass" : "2.000"}


def test_create_planet_happy_path(client):
    EXPECTED_PLANET = {
        "name": "test_name",
        "description": "test_description",
        "mass": 1,
        }

    response = client.post("/planets", json=EXPECTED_PLANET)
    response_body = response.get_data(as_text=True)

    actual_planet = Planet.query.get(1)
    assert response.status_code == 201
    assert response_body == f"New planet {EXPECTED_PLANET['name']} successfully created, biatch!"
    assert actual_planet.name == EXPECTED_PLANET["name"]
    assert actual_planet.description == EXPECTED_PLANET["description"]
    assert actual_planet.mass == EXPECTED_PLANET["mass"]


def test_get_none_existing_planet_returns_404(client, get_planets):
    response = client.get("/planets/404")

    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {'message': 'Planet 404 was not found, sucker!'}

def test_get_invalid_planet_returns_400(client, get_planets):
    response = client.get("/planets/noob")

    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == {'message': 'Planet noob is invalid, sucker!'}

def test_get_all_planets_returns_array_of_planets_and_200(client, get_planets):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 2
    assert response_body == [{"id" : 1, "name" : "test_name_2", "description" : "test_description_2", "mass" : "2.000"},
                            {"id" : 2, "name" : "test_name_3", "description" : "test_description_3", "mass" : "3.000"}]

def test_delete_one_planet(client, get_planets):
    response = client.delete("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {'message': 'Planet <Planet 1> succesfully deleted, biatch!'}

def test_update_one_planet(client, get_planets, one_planet):
    response = client.put("/planets/2", json=one_planet)
    response_body = response.get_json()
    response_array = client.get("/planets")
    updated_array = response_array.get_json()

    assert response.status_code == 200
    assert response_body == {'message': 'Planet <Planet 2> succesfully updated, biatch!'}
    assert updated_array == [{'id': 1, 'name': 'test_name_2', 'description': 'test_description_2','mass': '2.000'},
                            {'id': 2, 'name': 'test_name_1', 'description': 'test_description_1', 'mass': '1.000'}]