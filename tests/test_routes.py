def test_get_all_planets(client, two_saved_planets):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 2


def test_get_all_planets_no_records(client):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 0


def test_get_one_planet(client, two_saved_planets):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Mercury",
        "description": "The smallest planet; pitted and streaky, brownish-gray",
        "distance_from_the_sun": 0.39
    }


def test_get_one_planet_no_records(client):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body["message"] == "Planet with id 1 was not found"


def test_create_one_planet(client):
    response = client.post("/planets", json={
        "name": "Earth",
        "description": "A beautiful blue-green planet with life-supporting atmosphere",
        "distance_from_the_sun": 1.00
    })
    response_body = response.get_data(as_text=True)

    assert response.status_code == 201
    assert response_body == "Planet Earth successfully created"