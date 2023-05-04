def test_get_all_planets_with_no_records(client):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet(client, two_planets):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Nebula",
        "description": "Fake planet for testing purposes",
        "solar_day": 420.0
    }

def test_get_one_planet_no_data_404(client):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body["message"] == "planet 1 not found"

def test_get_one_planet_invalid_id_400(client):
    response = client.get("/planets/WALLA-WALLA")
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body["message"] == "planet WALLA-WALLA invalid"

def test_post_one_planet(client, walla_walla):
    response = client.post("/planets", json=walla_walla)

    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == "Planet Walla-Walla created successfully."

def test_delete_one_planet(client, two_planets):
    response = client.delete("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == "Planet Nebula was deleted."

def test_update_one_planet(client, two_planets, walla_walla):
    response = client.put("/planets/1", json=walla_walla)
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == "Planet Walla-Walla updated successfully."
