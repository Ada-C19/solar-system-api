def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_all_planets_with_two_records(client, two_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {"id": 1,"name":"Venus","description":"Gassy love goddess","place":2}
#{"id" : 2, "name":"Earth","description" : "le home", "place": 3}]         