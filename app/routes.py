from app import db
from app.models.Planet import Planet
from flask import Blueprint, jsonify, make_response, request, abort 


planets = Blueprint("planets", __name__, url_prefix="/planets")

@planets.route("", methods=["POST"])
def handle_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                    description=request_body["description"],
                    place=request_body["place"])
    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} succesfully created",201)


@planets.route("", methods=["GET"])
def return_all_planets():

    planets= Planet.query.all()
    planet_response = []

    for planet in planets:
        planet_response.append({
            "id": planet.id,
            "name": planet.name,
            "description":planet.description,
            'place':planet.place
        })
    return jsonify(planet_response)

def handle_planet_id(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"planet {planet_id} invalid"}, 400))
    
    planet = Planet.query.get(planet_id)
    if not planet:
            abort(make_response({"message":f"planet {planet_id} not found"}, 404))
    return planet
    

@planets.route("/<planet_id>", methods=["GET"])
def returns_one_planet_info(planet_id):
    planet= handle_planet_id(planet_id)
    planet_response= ({
            "id": planet.id,
            "name": planet.name,
            "description":planet.description,
            'place':planet.place
        })
    return (planet_response)


@planets.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = handle_planet_id(planet_id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.place = request_body["place"]

    db.session.commit()

    return make_response(f"Planet {planet.id} successfully updated")

@planets.route("/<planet_id>", methods=["DELETE"])

def delete_planet(planet_id):
    planet = handle_planet_id(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet #{planet.id} succesfully deleted")