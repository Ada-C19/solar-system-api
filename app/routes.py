from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, color):
        self.id = id
        self.name = name
        self.description = description
        self.color = color

planets = [
    Planet(1, "Mercury", "hot", "grey"), 
    Planet(2, "Venus", "Planet of love", "orange"), 
    Planet(3, "Earth", "Home", "blue-green"),
    Planet(4, "Mars", "volatile", "red"), 
    Planet(5, "Jupiter", "stormy", "beige"), 
    Planet(6, "Saturn", "the rings", "yellow"), 
    Planet(7, "Uranus", "the single ring", "light blue"), 
    Planet(8, "Neptune", "far away", "blue") 
]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods = ["GET"])
def handle_planets():
    planets_response = []
    for planet in planets:
        planets_response.append(dict(
            id = planet.id,
            name = planet.name, 
            description = planet.description, 
            color = planet.color
        ))
    return jsonify(planets_response), 200

