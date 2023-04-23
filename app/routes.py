from flask import Blueprint, jsonify


class Planet:
    def __init__(self, id, name, description, association):
        self.id = id
        self.name = name
        self.description = description
        self.association = association


planets = [
    Planet(1, "Mercury", "smallest planet", "Wednesday"),
    Planet(2, "Mars", "spicy, red one", "Tuesday"),
    Planet(3, "Jupiter", "biggest planet", "Thursday"),
    Planet(4, "Venus", "hottest planet", "Friday"),
    Planet(5, "Saturn", "the one with the rings", "Saturday")
]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")


@planets_bp.route("", methods=["GET"])
def handle_planets():
    planets_list = []
    for planet in planets:
        planets_list.append(dict(
            id=planet.id,
            name=planet.name,
            description=planet.description,
            weekday=planet.association
        ))
    return jsonify(planets_list)
