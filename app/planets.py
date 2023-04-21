from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, size):
        self.id  = id
        self.name = name
        self.description = description
        self.size = size


planet1 = Planet(1, "Mercury", "It has an average distance of about 57 million kilometer from the sun", 4879.4)

planet2 = Planet(2, "Venus", "It has an average distance of about 108 million kilometer from the sun", 12104)

planet3 = Planet(
    3, "Earth", "It has an average distance of about 150 million kilometer from the sun", 12742)

planet4 = Planet(
    4, "Mars", "It has an average distance of about 228 million kilometer from the sun", 6779)

planet5 = Planet(
    5, "Jupiter", "It has an average distance of about 779 million kilometer from the sun", 139820)

planet6 = Planet(
    6, "Saturn", "It has an average distance of about 1.46 million kilometer from the sun", 116460)

planet7 = Planet(
    7, "Uranus", "It has an average distance of about 2.88 million kilometer from the sun", 50724)

planet8 = Planet(
    8, "Neptune", "It has an average distance of about 4.5 million kilometer from the sun", 49244)


planet_list = [planet1, planet2, planet3, planet4, planet5, planet6, planet7, planet8]

planet_bp = Blueprint("planet", __name__, url_prefix="/planet")


@planet_bp.route("", methods=["GET"])
def get_planets():
    response = []
    for planet in planet_list:
        planet_dict = {"id": planet.id,
                       "name": planet.name,
                       "description": planet.description,
                       "size": planet.size
                       }
        response.append(planet_dict)
    return jsonify(response), 200


@planet_bp.route("/<id>", methods=["GET"])
def get_one_planet(id):
    try:
        planet_id = int(id)
    except ValueError:
        return {"message": f"id {id} is invalid"}, 400
    
    for planet in planet_list:
        if planet_id == planet.id:
            return jsonify({"id": planet.id,
                    "name": planet.name,
                    "description": planet.description,
                    "size": planet.size
                    }), 200
    return {"message":f"id {planet_id} not found"}, 404
