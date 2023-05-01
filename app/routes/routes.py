from flask import Blueprint, jsonify, request, make_response, abort
from app import db
from app.models.moon import Moon
from app.models.planet import Planet

solar_system_planet = Blueprint("solar_system_planet", __name__, url_prefix="/solar_system/planet")

@solar_system_planet.route("", methods=["POST"])
def add_planet():
    request_body = request.get_json()
    new_planet = Planet(
        name = request_body["name"],
        radius = request_body["radius"],
        description = request_body["description"]
    )
    
    db.session.add(new_planet)
    db.session.commit()

    return make_response({"message": f"Planet {new_planet.name} has been added, with the id: {new_planet.id}"}, 201)

@solar_system_planet.route("", methods=["GET"])
def get_planets():
    return_list = []
    all_planets = Planet.query.all()
    for planet in all_planets:
        return_list.append({
            "id": planet.id,
            "name": planet.name,
            "radius": planet.radius,
            "description": planet.description
        })
    return jsonify(return_list), 200

@solar_system_planet.route("/<planet_id>", methods=["GET"])
def get_planet_by_id(planet_id):
    planet = verify_planet_id(planet_id)
    return {
            "id": planet.id,
            "name": planet.name,
            "radius": planet.radius,
            "description": planet.description
        }

@solar_system_planet.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = verify_planet_id(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response({"message": f"Planet {planet.id} has been deleted"}, 200)

@solar_system_planet.route("/<planet_id>", methods=["PUT"])
def update(planet_id):
    planet = verify_planet_id(planet_id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.radius = request_body["radius"]
    planet.description = request_body["description"]

    db.session.commit()

    return make_response({"message": f"Planet {planet.id} has been updated"}, 200)

def verify_planet_id(planet_id):
    try: 
        planet_id = int(planet_id)
    except ValueError:
        abort(make_response({"message": f"Planet {planet_id} is invalid"}, 400))
    all_planets = Planet.query.all()
    for planet in all_planets:
        if planet.id == planet_id:
            return planet
    abort(make_response({"message": "Planet {planet_id} is not found"}, 404))

solar_system_moon = Blueprint("solar_system_moon", __name__, url_prefix="/solar_system/moon")

@solar_system_moon.route("", methods=["POST"])
def add_moon():
    request_body = request.get_json()
    new_moon = Moon(
        name = request_body["name"],
        radius = request_body["radius"],
        planet_id = request_body["planet_id"]
    )
    
    db.session.add(new_moon)
    db.session.commit()

    return make_response({"message": f"Moon {new_moon.name} has been added, with the id: {new_moon.id}"}, 201)

@solar_system_moon.route("", methods=["GET"])
def get_moons():
    return_list = []
    all_moons = Moon.query.all()
    for moon in all_moons:
        return_list.append({
            "id": moon.id,
            "name": moon.name,
            "radius": moon.radius,
            "planet name": moon.planet_id
        })
    return jsonify(return_list), 200

@solar_system_moon.route("/<moon_id>", methods=["GET"])
def get_moon_by_id(moon_id):
    moon = verify_moon_id(moon_id)
    return {
            "id": moon.id,
            "name": moon.name,
            "radius": moon.radius,
            "planet name": moon.planet_id
        }

@solar_system_moon.route("/<moon_id>", methods=["DELETE"])
def delete_planet(moon_id):
    moon = verify_moon_id(moon_id)

    db.session.delete(moon)
    db.session.commit()

    return make_response({"message": f"Moon {moon.id} has been deleted"}, 200)

@solar_system_moon.route("/<moon_id>", methods=["PUT"])
def update(moon_id):
    moon = verify_moon_id(moon_id)
    request_body = request.get_json()

    moon.name = request_body["name"]
    moon.radius = request_body["radius"]
    moon.planet_id = request_body["planet_id"]

    db.session.commit()

    return make_response({"message": f"Moon {moon.id} has been updated"}, 200)

def verify_moon_id(moon_id):
    try: 
        moon_id = int(moon_id)
    except ValueError:
        abort(make_response({"message": f"Moon {moon_id} is invalid"}, 400))
    all_moons = Moon.query.all()
    for moon in all_moons:
        if moon.id == moon_id:
            return moon
    abort(make_response({"message": f"Moon {moon_id} is not found"}, 404))

