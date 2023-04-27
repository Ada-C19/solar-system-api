from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.planet import Planet


# class Planet:
#     def __init__(self, id, name, description, color):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.color = color

# planets = [
#     Planet(1,"Earth","Only planet with liquid water", "blue"),
#     Planet(2,"Jupiter","Twice as massive tha the other planets combined","pink"),
#     Planet(3,"Mars","Is where aliens live","orange")
#     ]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

# def validate_planet(planet_id):
#     #handle invalid planet_id, return 400
#     try:
#         planet_id = int(planet_id)
#     except:
#         abort(make_response({ "message":f"planet {planet_id} invalid"}, 400))

#     #search for planet_in in data, return planet
#     for planet in planets:
#         if planet.id == planet_id:
#             return planet

#     #return a 404 for non-existing planet
#     abort(make_response({"message":f"planet {planet_id} not found"}, 404))
    
@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                        description=request_body["description"],
                        color=request_body["color"])
    
    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)


@planets_bp.route("",methods=["GET"])
def read_all_planets():
    
    planets = Planet.query.all()

    planets_response = [vars(planet) for planet in planets]

    return jsonify(planets_response), 200

# @planets_bp.route("/<planet_id>", methods=["GET"])
# def single_planet(planet_id):
#     planet = validate_planet(planet_id)
        
#     return {
#                 "id":planet.id,
#                 "name":planet.name,
#                 "description":planet.description,
#                 "color":planet.color
#             }
    