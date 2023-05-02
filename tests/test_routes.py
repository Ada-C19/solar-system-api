def test_get_all_planets_no_records(client):
    response = client.get("/planets")

    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 0