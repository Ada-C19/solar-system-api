from os import abort
from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request

planet_bp = Blueprint("planet", __name__, url_prefix="/planets")

@planet_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet.from_dict(request_body)

    db.session.add(new_planet)
    db.session.commit()
    return make_response(jsonify(new_planet.to_dict()), 201)

@planet_bp.route("", methods=["GET"])
def read_all_planets():
    name_query = request.args.get("name")
    description_query = request.args.get("description")
    diameter_query = request.args.get("diameter")
    planet_query = Planet.query

    if name_query:
        planet_query = planet_query.filter_by(name=name_query)
    if description_query:
        planet_query = planet_query.filter(Planet.description.ilike(f"%{description_query}%"))
    if diameter_query:
        planet_query = planet_query.filter_by(diameter=diameter_query)

    planets_response = [planet.to_dict() for planet in planet_query]
    return make_response(jsonify(planets_response), 200) 

@planet_bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = Planet.validate_planet(planet_id)
    return make_response(jsonify(planet.to_dict()), 200)

@planet_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = Planet.validate_planet(planet_id)
    
    request_body = request.get_json()
    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.diameter = request_body["diameter"]
    db.session.commit()

    return make_response(jsonify(planet.to_dict()), 200)

@planet_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = Planet.validate_planet(planet_id)
    db.session.delete(planet)
    db.session.commit()

    return make_response(jsonify({"message":f"Planet #{planet.id} successfully deleted"}))