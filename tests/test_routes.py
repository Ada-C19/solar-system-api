import pytest


def test_get_one_planet(client, two_planets):
    # act
    response = client.get("/planet/1")
    response_body = response.get_json()
    
    #assert
    assert response.status_code == 200
    assert response_body == {"id":1, "name":"Venus","description":"this is Venus","size":6666}


def test_get_one_planet_with_no_record(client):
    # act
    response = client.get("/planet")
    response_body = response.get_json()
    
    #assert
    assert response.status_code == 200
    assert response_body == []


def test_no_record_return_404(client):
    # act
    response = client.get("/planet/1")
    response_body = response.get_json()

    # assert
    assert response.status_code == 404


def test_get_all_planets(client, two_planets):
    # act
    response = client.get("/planet")
    response_body = response.get_json()
    
    #assert
    assert response.status_code == 200
    assert response_body == [{"id":1, "name":"Venus","description":"this is Venus","size":6666},
                             {"id":2, "name":"Mars","description":"this is Mars","size":9999}
                             ]
    
def test_create_one_planet(client):
    #act
    response = client.post("/planet", json={
        "name":"earth",
        "description":"this is earth",
        "size": 10000
    })

    response_body = response.get_json()

    #assert
    assert response.status_code == 201

    assert "id" in response_body
    
 # delete
def test_delete_planet(client, two_planets):
    response = client.delete("/planet/1")

    response_body = response.get_json()

    assert response.status_code == 200
    assert "planet 1 has been deleted" in response_body["message"]


#PUT TEST
def test_put_planet(client, two_planets):
    response = client.put("/planet/1", json={
        "name": "sample",
        "description": "updating planet",
        "size": 231
    })

    response_body = response.get_json()

    assert response.status_code == 200
    assert "planet 1 has been updated" in response_body["message"]
