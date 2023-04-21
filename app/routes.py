from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, diameter):
        self.id = id
        self.name = name
        self.description = description
        self.diameter=diameter

planets = [
    Planet(1, "Mercury", "closest to sun", 3031.9),
    Planet(2, "Venus", "hottest planet", 7520.8),
    Planet(3, "Earth", "our home planet", 7917.5),
    Planet(4, "Mars", "red planet", 4212.3)
]

planet_bp = Blueprint("planet", __name__, url_prefix="/planets")

@planet_bp.route("", methods=["GET"])
def read_planets():
    planet_list = [make_planet_dict(planet) for planet in planets]
    return jsonify(planet_list)

def make_planet_dict(planet):
    return dict(
        id=planet.id,
        name=planet.name,
        description=planet.description,
        diameter=planet.diameter
    )


