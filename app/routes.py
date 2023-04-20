from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, size):
        self.id = id
        self.name = name
        self.description = description
        self.size = size

mercury = Planet(1, "Mercury", "First planet from the sun", 3032)
venus = Planet(2, "Venus", "Second planet from the sun", 7521)
earth = Planet(3, "Earth", "Third planet from the sun", 7918)

planet_list = [mercury, venus, earth]

planet_bp = Blueprint("planet", __name__, url_prefix="/planet")

@planet_bp.route("", methods= ['GET'])
def get_planets():
    response = []
    for planet in planet_list: 
        planet_dict = {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "size": planet.size
        }
        response.append(planet_dict)
    return jsonify(response), 200