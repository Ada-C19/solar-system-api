def test_get_all_planets_with_no_records(client):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 0
    assert response_body == []


def test_get_all_planets_with_two_records(client, two_saved_planets):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 2
    assert response_body[0] == {
        "id": 1,
        "name": "Mercury",
        "description": "The smallest planet; pitted and streaky, brownish-gray",
        "distance_from_the_sun": 0.39
    }
    assert response_body[1] == {
        "id": 2,
        "name": "Venus",
        "description": "A fireball with temperatures hot enough to melt lead, covered in thick clouds",
        "distance_from_the_sun": 0.72
    }


def test_get_all_planets_with_name_query_matching_none(client, two_saved_planets):
    data = {"name": "Eros"}
    response = client.get("/planets", query_string=data)
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []


def test_get_all_planets_with_name_query_matching_one(client, two_saved_planets):
    data = {"name": "Venus"}
    response = client.get("/planets", query_string=data)
    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 1
    assert response_body[0] == {
        "id": 2,
        "name": "Venus",
        "description": "A fireball with temperatures hot enough to melt lead, covered in thick clouds",
        "distance_from_the_sun": 0.72
    }


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


def test_get_one_planet_missing_record(client, two_saved_planets):
    response = client.get("/planets/100")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {"message": "Planet with id 100 was not found"}


def test_get_one_planet_invalid_id(client, two_saved_planets):
    response = client.get("planets/faraway")
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == {"message": "Planet with id faraway is invalid"}


def test_create_one_planet(client):
    response = client.post("/planets", json={
        "name": "Earth",
        "description": "A beautiful blue-green planet with life-supporting atmosphere",
        "distance_from_the_sun": 1.00
    })
    response_body = response.get_data(as_text=True)

    assert response.status_code == 201
    assert response_body == "Planet Earth successfully created"