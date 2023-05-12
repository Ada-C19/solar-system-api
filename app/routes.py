from flask import Blueprint, jsonify, abort, make_response, request
from app.models.planets import *


planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except:
#         abort(make_response({"message":f"planet {planet_id} invalid"}, 400))
    
#     for planet in planets:
#         if planet_id == planet.id:
#             return planet
#     abort(make_response({"message":f"planet {planet_id} not found"}, 404))

# @planets_bp.route("", methods=["GET"])
# def read_all_planets():
#     planets_response = []
#     # for planet in planets:
#     #     planets_response.append(planet.to_dict())
#     return jsonify(planets_response)

# @planets_bp.route("/<planet_id>", methods=["GET"])
# def read_one_planet(planet_id):
#     planet = validate_planet(planet_id)
#     return planet.to_dict()

