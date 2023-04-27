from flask import Blueprint, jsonify, request
from app import db
from app.models.planet import Planet

# class Planet:
#     def __init__(self, id, name, description, size):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.size = size

# mercury = Planet(1, "Mercury", "First planet from the sun", 3032)
# venus = Planet(2, "Venus", "Second planet from the sun", 7521)
# earth = Planet(3, "Earth", "Third planet from the sun", 7918)

# planet_list = [mercury, venus, earth]

planet_bp = Blueprint("planet", __name__, url_prefix="/planet")

@planet_bp.route("", methods=["POST"])
def add_planet():
    request_body = request.get_json()
    new_planet = Planet(name = request_body["name"], description = request_body["description"], size = request_body["size"])

    db.session.add(new_planet)
    db.session.commit()

    return {"id": new_planet.id}, 201

@planet_bp.route("", methods= ['GET'])
def get_planets():
    response = []
    all_planets = Planet.query.all()
    for planet in all_planets: 
        response.append(planet.to_dict())

    return jsonify(response), 200

# @planet_bp.route("/<id>", methods=["GET"])
# def get_one_planet(id):
#     try: 
#         planet_id = int(id)
#     except ValueError:
#         return {"message": f"Invalid id: {id}"}, 400

#     for planet in planet_list:
#         if planet.id == planet_id:
#             return {
#                 "id": planet.id,
#                 "name": planet.name,
#                 "description": planet.description,
#                 "size": planet.size
#             }, 200
    
#     return {"message": f"{planet_id} not found"}, 404