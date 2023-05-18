def test_get_one_planet(client, two_saved_planets):
    #Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert response_body == {
                "id":1,
                "name":"Mars", 
                "description":"where aliens live",
                "color":"red"
    }

def test_get_one_planet_empty_db_returns_404(client):
    response = client.get("/planets/1")

    assert response.status_code == 404

def test_get_all_planets(client, two_saved_planets):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [{
        "id":1,
        "name":"Mars", 
        "description":"where aliens live",
        "color":"red"}, 
        {"id":2,
        "name":"Jupiter", 
        "description":"really big",
        "color":"orange"}]
    
def test_create_one_planet(client):
    # Act
    response = client.post("/planets", json={
        "name":"Pluto", 
        "description":"very small",
        "color":"grey"
    })
    response_body = response.get_json()


    # Assert
    assert response.status_code == 201
    assert response_body ==  "Planet Pluto successfully created"