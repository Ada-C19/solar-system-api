def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet_with_two_records(client, two_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {"id": 1,"name":"Venus","description":"Gassy love goddess","place":2}
#{"id" : 2, "name":"Earth","description" : "le home", "place": 3}]  

# #GET /planets/1 with no data in test database (no fixture) returns a 404   
def test_empty_database_returns_404(client):

    #act
    response = client.get("planets/1")
    response_body = response.get_json()
    #assert   
    assert response.status_code == 404
    assert response_body == {"message":"planet 1 not found"}

def test_get_planets_with_two_records(client, two_planets):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [{"id": 1,"name":"Venus","description":"Gassy love goddess","place":2},{"id" : 2, "name":"Earth","description" : "le home", "place": 3}]  

#POST /planets with a JSON request body returns a 201

def test_JSON_request_returns_201(client, two_planets):

    response = client.post("/planets", json={
        "name": "Venus",
        "description":"Gassy love goddess",
        "place":2})

    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == "Planet Venus succesfully created"
    
