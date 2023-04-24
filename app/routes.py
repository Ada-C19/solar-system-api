from flask import Blueprint, jsonify, abort, make_response

# Define a Planet class with the attributes id, name, 
# and description, and one additional attribute

class Planet:
    def __init__(self, id, name, description, solar_day):
        self.id = id
        self.name = name
        self.description = description
        self.solar_day = solar_day

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
            solar_day=self.solar_day
        )

planets = [
    Planet(1, "Mercury", "smallest planet", 176.0),
    Planet(2, "Venus", "planet of love", 243.0),
    Planet(3, "Earth", "home planet", 1.0),
    Planet(4, "Mars", "red planet", 1.25),
    Planet(5, "Jupiter", "largest planet", 0.42),
    Planet(6, "Saturn", "ring planet", .45),
    Planet(7, "Uranus", "coldest planet", .71),
    Planet(8, "Neptune", "not visible to the naked eye", .67),
    Planet(9, "Pluto", "unqualified planet", 6.375)
    ]

        # Wave 2
        # read one planet
        # return 400 for invalid id
        # return 404 for non existing planet
planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])  
def handle_planets():
    results = []    
    for planet in planets:
        results.append(planet.to_dict())

    return jsonify(results)

@planets_bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):
    planet = validate_planet(planet_id)

    return planet.to_dict()


def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"planet {planet_id} invalid"}, 400))

    for planet in planets:
        if planet.id == planet_id:
            return planet

    abort(make_response({"message":f"planet {planet_id} not found"}, 404))