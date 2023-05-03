def test_get_all_planets_with_empty_db_returns_empty_list(client):
    # ARRANGE IS INSIDE CONFTEST
    # ACT
    response = client.get('/planets')
    response_body = response.get_json()

    # ASSERT
    assert response_body == []
    assert response.status_code == 200