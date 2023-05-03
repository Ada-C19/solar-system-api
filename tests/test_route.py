import pytest 

def test_get_all_planets(client, two_planets):
    response = client.get("/solar_system/planet")

    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == [
        {"id": 1, "name": "mercury", "radius": 1516, "description": "I am the smallest planet in our solar system"},
        {"id": 2, "name": "venus", "radius": 3760, "description": "I spin in the opposite direction from Earth"}]
    
def test_post_creates_planet(client):
    response = client.post("/solar_system/planet", json = {"name": "mercury", "radius": 1516, "description": "I am the smallest planet in our solar system"})
    
    response_body = response.get_json()
    
    assert response.status_code == 201
    assert "Planet mercury has been added, with the id: 1" in response_body["message"]

def test_get_one_planet(client, two_planets):
    response = client.get("/solar_system/planet/1")

    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {"id": 1, "name": "mercury", "radius": 1516, "description": "I am the smallest planet in our solar system"}
    
def test_delete_one_planet(client, two_planets):
    response = client.delete("/solar_system/planet/1")

    response_body = response.get_json()

    assert response.status_code == 200
    assert "Planet 1 has been deleted" in response_body["message"]