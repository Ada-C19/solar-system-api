from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.planet import Planet
from .routes_helpers import validate_model


bp = Blueprint("planets", __name__, url_prefix="/planets")

#GET ALL ENDPOINT
@bp.route("", methods=["GET"])
def get_all_planets():
    
    rating_param = request.args.get("rating")

    planet_query = Planet.query
    
    if rating_param:
        planet_query = planet_query.filter_by(rating=rating_param)
    
    planets_list = [planet.to_dict() for planet in planet_query]

    return jsonify(planets_list)

# CREATE ENDPOINT
@bp.route("", methods=["POST"])
def create_planet():
    request_body=request.get_json()

    new_planet = Planet.from_dict(request_body)

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created!", 201)

# GET ONE ENDPOINT
@bp.route("/<id>", methods=["GET"])
def handle_planet(id):
    planet = validate_model(Planet, id)

    return jsonify(planet.to_dict()), 200

# UPDATE ONE ENDPOINT
@bp.route("/<id>", methods=["PUT"])
def update_planet(id):
    planet = validate_model(Planet, id)
    request_body = request.get_json()

    planet.id = request_body["id"]
    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.rating = request_body["rating"]
    
    db.session.commit()

    return make_response(f"Planet {planet.name} successfully updated", 200)

# DELETE ONE ENDPOINT
@bp.route("/<id>", methods=["DELETE"])
def delete_planet(id):
    planet = validate_model(Planet, id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet {planet.name} successfully deleted", 200)



