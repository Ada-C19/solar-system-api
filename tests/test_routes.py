def test_get_all_planets_no_record(client):
    response = client.get("/planets")
    response_body = response.get_json()
    
    # assert
    assert response.status_code == 200
    assert response_body == []