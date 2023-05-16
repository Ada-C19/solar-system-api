
def test_len_of_empty_list(client):
    response = client.get("/planets")

    assert response.status_code == 200
    assert response.get_json() == []


##1. `GET` `/planets/1` returns a response body that matches our fixture
def test_get_one_planet_by_id(client, get_one_planet):
    # act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Saturn",
        "description": "Planet has rings."
    }



##2. `GET` `/planets/1` with no data in test database (no fixture) returns a `404`
def test_get_one_planet_not_found(client):
    # act
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {"message": "planet 1 not found"}





##3. `GET` `/planets` with valid test data (fixtures) returns a `200` with an array including appropriate test data
def test_read_all_planets_returns_ok(client, read_all_planets):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert isinstance(response_body, list)
    assert len(response_body) == 2
    
    
    
    # assert response_body == [
    #     {
    #     "description": "Planet has storms the size of earth!",
    #     "id": 2,
    #     "name": "Jupiter" 
    #     },
    #     {
    #     "description": "This planet has rings.",
    #     "id": 1,
    #     "name": "Saturn"
    #     }
    # ]




##4. `POST` `/planets` with a JSON request body returns a `201`
def test_post_one_book(client):
    response = client.post("/planets", json={
        "name": "Venus",
        "description": "Girls are made here!"
    })
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == "Planet Venus successfully created"