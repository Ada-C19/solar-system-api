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

@planets_bp.route("/<planet_id>", methods=["GET"])
def single_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except: return { "message":f"planet {planet_id} invalid"}, 400
    
    for planet in planets:
        if planet.id == planet_id:
            return {
                "id":planet.id,
                "name":planet.name,
                "description":planet.description,
                "color":planet.color
            }
        
    return { "message":f"planet {planet_id} not found"}, 404
    