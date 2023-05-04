def test_get_all_planets_empty_200(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

# 1 `GET` `/planets/1` returns a response body that matches our fixture

def test_get_one_planet(client, two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    
    assert response_body == {
            "id": 1,
            "name": "Venus",
            "description": "hot enough to melt lead n ur heart </3",
            "color": "she lil' rusty :("
        }


# 2 `GET` `/planets/1` with no data in test database (no fixture) returns a `404`

def test_get_one_planet_empty_404_status_code(client):
    # Act
    response = client.get("/planets/1")

    # Assert
    assert response.status_code == 404
    
# 3 `GET` `/planets` with valid test data (fixtures) returns a `200` with an array including appropriate test data
def test_get_all_planets(client, two_saved_planets):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()


    # Assert
    assert response.status_code == 200
    assert response_body == [
            {"id": 1,
            "name": "Venus",
            "description": "hot enough to melt lead n ur heart </3",
            "color": "she lil' rusty :("},
            {"id": 2,
            "name": "Saturn",
            "description": "bling bling rings",
            "color": "she cute pink :("}
    ]
    
# 4 `POST` `/planets` with a JSON request body returns a `201`

def test_create_one_planet(client):
        new_planet = dict(
        name="Earth",
        description="loud",
        color="blue & green"
    )
    # Act
        response = client.post("/planets", json=new_planet)
        response_body = response.get_data(as_text=True)

        # Assert
        assert response.status_code == 201
       