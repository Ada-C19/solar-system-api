def test_get_all_planets_with_empty_db_returns_empty_list(client):
    # ARRANGE IS INSIDE CONFTEST
    # ACT
    response = client.get('/planets')
    response_body = response.get_json()

    # ASSERT
    assert response_body == []
    assert response.status_code == 200


def test_get_one_planet_returns_correct_planet(client, two_planets):
    # ACT
    response = client.get('/planets/1')
    response_body = response.get_json()

    # ASSERT
    assert response.status_code == 200
    assert response_body == {   
            "id": 1,
            "name": "Furby",
            "description": "Purple",
            "distance from sun": 17
    }

def test_get_one_planet_empty_db_returns_404(client):
    response = client.get("/planets/1")
    assert response.status_code == 404


def test_get_all_planets_returns_200(client, two_planets):
    # ACT
    response = client.get('/planets')
    response_body = response.get_json()

    # ASSERT
    assert response.status_code == 200
    assert response_body == [
        {   
            "id": 1,
            "name": "Furby",
            "description": "Purple",
            "distance from sun": 17
        },
        {   
            "id": 2, 
            "name": "Squiggles", 
            "description": "Orange", 
            "distance from sun": 29
        }]
    
def test_post_one_planet_creates_planet_in_db(client):
    response = client.post("/planets", json={
            "name": "Earth", 
            "description": "Blue", 
            "distance from sun": 2
        }
    )
    print ("testing")
    response_body = response.get_json()
    print(response_body)
    assert response.status_code == 201
    
    # print(response_body["name"])
    # assert response_body["id"] == 
    # assert response_body["name"] == "Earth"
    # assert "msg" in response_body