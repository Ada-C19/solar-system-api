import pytest


def test_get_one_planet(client, two_planets):
    # act
    response = client.get("/planet/1")
    response_body = response.get_json()
    
    #assert
    assert response.status_code == 200
    assert response_body == {"id":1, "name":"Venus","description":"this is Venus","size":6666}
