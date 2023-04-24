from flask import Blueprint, jsonify

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

class Planet:
    def __init__(self, id, name, description, num_moons):
        self.id = id,
        self.name = name,
        self.description = description,
        self.num_moons = num_moons

planets = [
    Planet(1, "Mercury", "It's the first planet in our solar system", 0),
    Planet(2, "Venus", "It's the second planet in our solar system", 0),
    Planet(3, "Earth", "It's the third planet in our solar system", 1)
]

@planets_bp.route("", methods=["GET"])
def handle_planets():
    planets_response = []
    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "num_moons": planet.num_moons
        })
    return jsonify(planets_response)