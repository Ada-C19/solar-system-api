from app.models.planet import Planet
def test_get_all_planets_no_record(client):
    response = client.get("/planets")
    response_body = response.get_json()
    
    # assert
    assert response.status_code == 200
    assert response_body == []
    
def test_get_one_planet_with_test_data(client, saved_planets):
    response = client.get("/planets/1")
    response_body = response.get_json()
    
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Mercury",
        "description": "rocky planet",
        "form": "solid"
    }
def test_get_one_planet_with_no_data(client):
    response = client.get("/planets/1")
    response_body = response.get_json()
    
    assert response.status_code == 404
    assert response_body == {"message":"Planet 1 not found"}
    
def test_get_planets_with_valid_test_data(client, saved_planets):
    response = client.get("/planets")
    response_body = response.get_json()
    
    assert response.status_code == 200
    assert len(response_body) == 2
    assert response_body[0] == {"id":1, "name":"Mercury",
                                "description":"rocky planet", "form":"solid" }       

def test_create_one_planet(client):
    PLANET_DICT = {"name": "Saturn",
                   "description":"made of hydrogen",
                   "form":"gas"}
    response = client.post("/planets", json=PLANET_DICT)
    response_body = response.get_json()
    
    actual_planet = Planet.query.get(1)
    
    assert response.status_code == 201
    assert response_body == "Planet Saturn was created successfully"
    assert actual_planet.name == "Saturn"
    assert actual_planet.description == "made of hydrogen"
    assert actual_planet.form =="gas"