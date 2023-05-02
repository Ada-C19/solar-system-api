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
    assert response_body == {"message":"planet 1 not found"}