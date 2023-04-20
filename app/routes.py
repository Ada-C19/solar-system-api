from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, color):
        self.id = id
        self.name = name
        self.description = description
        self.color = color

planets = [
    Planet(1,"Earth","Only planet with liquid water", "blue"),
    Planet(2,"Jupiter","Twice as massive tha the other planets combined","pink"),
    Planet(3,"Mars","Is where aliens live","orange")
    ]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("",methods=["GET"])
def list_planets():
    planets_response = [vars(planet) for planet in planets]

    return jsonify(planets_response), 200
    