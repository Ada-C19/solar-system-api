from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request, abort
from .routes_helpers import validate_model

bp = Blueprint("planets", __name__, url_prefix="/planets")


@bp.route("/<id>", methods=["GET"])
def read_one_planet(id):
    planet = validate_model(Planet, id)

    return planet.to_dict()


@bp.route("", methods=["GET"])
def read_all_planets():
    name_query = request.args.get("name")

    if name_query:
        planets = Planet.query.filter_by(name=name_query)
    else:
        planets = Planet.query.all()

    planets_response = [Planet.to_dict(planet) for planet in planets]

    return jsonify(planets_response)


@bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet.from_dict(request_body)

    db.session.add(new_planet)
    db.session.commit()

    return make_response(jsonify(f'Planet {new_planet.name} successfully created.'), 201)


@bp.route("/<id>", methods=["PUT"])
def update_planet(id):
    planet = validate_model(Planet, id)
    request_body = request.get_json()

    Planet.from_dict(request_body)

    db.session.commit()

    return make_response(jsonify(f"Planet #{planet.id} successfully updated"))


@bp.route("/<id>", methods=["DELETE"])
def delete_planet(id):
    planet = validate_model(Planet, id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(jsonify(f"Planet #{planet.id} successfully deleted"))
