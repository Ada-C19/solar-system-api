from flask import Blueprint, jsonify, abort, make_response

class Planet:
    def __init__(self, id, name, description, color):
        self.id = id
        self.name = name
        self.description = description
        self.color = color

    def make_planet_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
            color=self.color
        )

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

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except: 
        abort(make_response({"message": f"Planet with id {planet_id} is invalid"}, 400))
    
    for planet in planets:
        if planet.id == planet_id:
            return planet
    
    return abort(make_response({"message": f"Planet with id {planet_id} was not found"}, 404))


@planets_bp.route("", methods = ["GET"])
def handle_planets():
    planets_response = []
    for planet in planets:
        planets_response.append(planet.make_planet_dict())
    return jsonify(planets_response), 200


@planets_bp.route("/<planet_id>", methods = ["GET"])
def handle_planet(planet_id):
    planet = validate_planet(planet_id)

    return planet.make_planet_dict()
