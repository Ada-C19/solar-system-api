from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request, abort
from .routes_helpers import validate_model



planets_bp = Blueprint("planets", __name__, url_prefix="/planets")


@planets_bp.route("", methods=["POST"])
def add_new_planet():
    request_body = request.get_json()

    new_planet = Planet.dict_to_model(request_body)


    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

@planets_bp.route("", methods=["GET"])
def get_all_planets():

    name_param = request.args.get("name")
    
    if name_param:
        planets = Planet.query.filter_by(name=name_param)
    else:
        planets = Planet.query.all()

    planets_list=[planet.make_planet_dict()for planet in planets]

    return jsonify(planets_list), 200

@planets_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet(planet_id):

    planet = validate_model(Planet, planet_id)

    return planet.make_planet_dict(), 200


@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet#{planet.id} successfully deleted")

@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet=validate_model(Planet, planet_id)
    request_body=request.get_json()

    if request_body.get("name") is None or request_body.get("description") is None or request_body.get("moons") is None:
        return make_response(f"some additional information needed to update planet {planet.name}",400)

    planet.name=request_body["name"]
    planet.description=request_body["description"]
    planet.moons=request_body["moons"]

    db.session.commit()

    return make_response(f"planet {planet.name} succesfully updated",200)

