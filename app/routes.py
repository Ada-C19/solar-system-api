from flask import Blueprint, jsonify
from app import db
from app.models.planet import Planet

# class Planet:
#     def __init__(self, id, name, description):
#         self.id = id
#         self.name = name
#         self.description = description

# mercury = Planet(1, "Mercury", "smallest planet, and hot")
# venus = Planet(2, "Venus", "small, the hottest")
# earth = Planet(3, "Earth", "medium, green, lush, home planet, in danger")
# mars = Planet(4, "Mars", "red, no water, also in danger")
# jupiter = Planet(5, "Jupiter", "largest, many moons")
# saturn = Planet(6, "Saturn", "cool rings, large")
# uranus = Planet(7, "Uranus", "large, funny name")
# neptune = Planet(8, "Neptune", "large, blue, cold")
# pluto = Planet(9, "Pluto", "dwarf planet, very cold")

# planet_list = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, pluto]

planet_bp = Blueprint("planet", __name__, url_prefix="/planet")

@planet_bp.route("", methods=["POST"])
def add_planet():
    request_body = request.get_json()
    new_planet = Planet(
        name = request_body["name"],
        description = request_body["description"],
        num_moons = request_body["num_moons"]
    )

    db.session.add(new_planet)
    db.session.commit()

    return {"id": new_planet.id}, 201

# @planet_bp.route("", methods=["GET"])
# def get_restaurants():
#     response = []
#     for planet in planet_list:
#         planet_dict = {
#             "id": planet.id,
#             "name": planet.name,
#             "description": planet.description
#         }
#         response.append(planet_dict)

#     return jsonify(response), 200

# @planet_bp.route("/<id>", methods=["GET"])
# def get_one_planet(id):
#     try:
#         planet_id = int(id)
#     except:
#         return {"message": f"invalid id: {id}"}, 400
    
#     for planet in planet_list:
#         if planet.id == planet_id:
#             return jsonify({
#             "id": planet.id,
#             "name": planet.name,
#             "description": planet.description}), 200
    
#     return jsonify({"message": f"id {planet_id} not found"}), 404