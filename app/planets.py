from flask import Blueprint, jsonify, request
from app import db
from app.model.planets_model import Planet


# planet1 = Planet(1, "Mercury", "It has an average distance of about 57 million kilometer from the sun", 4879.4)

# planet2 = Planet(2, "Venus", "It has an average distance of about 108 million kilometer from the sun", 12104)

# planet3 = Planet(
#     3, "Earth", "It has an average distance of about 150 million kilometer from the sun", 12742)

# planet4 = Planet(
#     4, "Mars", "It has an average distance of about 228 million kilometer from the sun", 6779)

# planet5 = Planet(
#     5, "Jupiter", "It has an average distance of about 779 million kilometer from the sun", 139820)

# planet6 = Planet(
#     6, "Saturn", "It has an average distance of about 1.46 million kilometer from the sun", 116460)

# planet7 = Planet(
#     7, "Uranus", "It has an average distance of about 2.88 million kilometer from the sun", 50724)

# planet8 = Planet(
#     8, "Neptune", "It has an average distance of about 4.5 million kilometer from the sun", 49244)


# planet_list = [planet1, planet2, planet3, planet4, planet5, planet6, planet7, planet8]

planet_bp = Blueprint("planet", __name__, url_prefix="/planet")


@planet_bp.route("", methods=["POST"])
def add_planet():
    request_body = request.get_json()
    new_planet = Planet(
        name = request_body['name'],
        description = request_body['description'],
        size = request_body['size']
    )
    db.session.add(new_planet)
    db.session.commit()

    return f"id{new_planet.id}", 201

@planet_bp.route("", methods=["GET"])
def get_planets():
    response = []
    all_planets = Planet.query.all()
    for planet in all_planets:
        response.append(planet.to_dict())
    return jsonify(response), 200


# @planet_bp.route("/<id>", methods=["GET"])
# def get_one_planet(id):
#     try:
#         planet_id = int(id)
#     except ValueError:
#         return {"message": f"id {id} is invalid"}, 400
    
#     for planet in planet_list:
#         if planet_id == planet.id:
#             return jsonify({"id": planet.id,
#                     "name": planet.name,
#                     "description": planet.description,
#                     "size": planet.size
#                     }), 200
#     return {"message":f"id {planet_id} not found"}, 404
