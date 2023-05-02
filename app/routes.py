from flask import Blueprint, jsonify, abort, make_response


class Planet:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

planets = [
    Planet(1, "Mercury", "Terrestrial planet closest to the sun. Smallest planet."),
    Planet(2, "Venus", "Terrestrial planet second from sun. Hot surface."),
    Planet(3, "Earth", "Third planet from the sun. Largest terrestrial planet."),
    Planet(4, "Mars", "Terrestrial planet fourth from the sun. Red planet."),
    Planet(5, "Jupiter", "First gas giant planet from the sun. Largest planet."),
    Planet(6, "Saturn", "Sixth planet from the sun. Gas giant planet with rings."),
    Planet(7, "Uranus", "Seventh planet from the sun. Ice giant planet."),
    Planet(8, "Neptune", "Furthest planet from the sun. Cold, blue gas giant planet.")
]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])
def handle_planets():
    planets_response = []
    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description
        })
    return jsonify(planets_response)

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"planet {planet_id} invalid"}, 400))
    
    for planet in planets:
        if planet_id == planet.id:
            return planet
    
    abort(make_response({"message":f"planet {planet_id} not found"}, 404))


@planets_bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):
    planet = validate_planet(planet_id)
    
    return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
    }
