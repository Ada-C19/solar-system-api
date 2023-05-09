from flask import Blueprint, jsonify, request, make_response, abort
from app import db
from app.model.moon import Moon




moon_bp = Blueprint("moon", __name__, url_prefix="/moon")

# CREATE


@moon_bp.route("", methods=["POST"])
def add_moon():
    request_body = request.get_json()
    new_moon = Moon.from_dict(request_body)

    db.session.add(new_moon)
    db.session.commit()

    planet_dict = {
        "id": new_moon.id,
        "name": new_moon.name,
        "description": new_moon.description,
        "size": new_moon.size
    }

    return jsonify(planet_dict), 201


# GET ALL
@moon_bp.route("", methods=["GET"])
def get_planets():
    response = []

   
    all_moons = Moon.query.all()

    for moon in all_moons:
        response.append(moon.to_dict())
        
    return jsonify(response), 200


# # GET ONE
# @moon_bp.route("/<id>", methods=["GET"])
# def get_one_pla(id):

#     planet = validate_planet(Planet, id)

#     return planet.to_dict(), 200
