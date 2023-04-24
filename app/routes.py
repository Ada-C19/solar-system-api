from flask import Blueprint, jsonify, abort, make_response


class Planet:
    def __init__(self, id, name, description, association):
        self.id = id
        self.name = name
        self.description = description
        self.association = association

    def make_planet_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
            association=self.association)


planets = [
    Planet(1, "Mercury", "smallest planet", "Wednesday"),
    Planet(2, "Mars", "spicy, red one", "Tuesday"),
    Planet(3, "Jupiter", "biggest planet", "Thursday"),
    Planet(4, "Venus", "hottest planet", "Friday"),
    Planet(5, "Saturn", "the one with the rings", "Saturday")
]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")


@planets_bp.route("/<id>", methods=["GET"])
def handle_planet(id):
    try:
        id = int(id)
    except ValueError:
        abort(make_response({'message': f'Planet {id} is invalid.'}, 400))

    for planet in planets:
        if planet.id == id:
            return planet.make_planet_dict()

    abort(make_response({'message': f'Planet {id} not found.'}, 404))


@planets_bp.route("", methods=["GET"])
def handle_planets():
    planets_list = []
    for planet in planets:
        planets_list.append(planet.make_planet_dict())
    return jsonify(planets_list)
