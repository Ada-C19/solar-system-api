from flask import Blueprint, jsonify, abort, make_response, request


planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def create_planets():
    request_body = request.get_json()
    new_planet = 

@planets_bp.route("", methods=["GET"])
def read_all_planets():
    planets_response = []

    for planet in planets:
        planets_response.append(planet.to_dict())
    return jsonify(planets_response)