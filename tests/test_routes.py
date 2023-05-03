def test_get_all_planets_with_empty_db_returns_empty_list(client):
    # ARRANGE IS INSIDE CONFTEST
    # ACT
    response = client.get('/planets')
    response_body = response.get_json()

    # ASSERT
    assert response_body == []
    assert response.status_code == 200





def test_get_one_planet_returns_correct_pkanet(client, two_planets):
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

def test_get_one_animal_empty_db_returns_404(client):
    response = client.get("/planets/1")
    assert response.status_code == 404


    