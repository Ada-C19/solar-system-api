from flask import Blueprint, jsonify, abort, make_response
from app.models.planet import Planet

# class Planet:
#     def __init__(self, id, name, description, color):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.color = color

# planets = [
#     Planet(1, "Earth", "habitable", "blue & green"),
#     Planet(2, "Venus", "hot", "yellowy orange"),
#     Planet(3, "Saturn", "beautiful ringlets", "light yellow"),
#     Planet(4, "Neptune", "furthest from the sun", "blue")
# ]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")


# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except:
#         abort(make_response({"message":f"planet {planet_id} invalid"}, 400))
    
#     for planet in planets:
#         if planet.id == planet_id:
#             return planet
        
#     abort(make_response({"message":f"planet {planet_id} not found"}, 404))


# # Endpoint to get all planets
# @planets_bp.route("", methods=["GET"])
# def handle_planets():
#     planets_response = []
#     for planet in planets:
#         planets_response.append({
#             "id": planet.id,
#             "name": planet.name,
#             "description": planet.description,
#             "color": planet.color
#         })
#     return jsonify(planets_response), 200

# # Endpoint to get a planet
# @planets_bp.route("/<planet_id>", methods=["GET"])
# def handle_planet(planet_id):
#     planet = validate_planet(planet_id)

#     return {
#         "id": planet.id,
#         "name": planet.name,
#         "description": planet.description,
#         "color": planet.color,
#     }

