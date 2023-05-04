from app import db
from flask import Blueprint, jsonify, abort, make_response, request
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
#VALIDATE PLANET HELPER FN
def validate_planet(planet_id): # ONLY TO GET & PUT ONE PLANET_ID
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"planet {planet_id} invalid"}, 400))
    
    planet = Planet.query.get(planet_id)

    if not planet:    
        abort(make_response({"message":f"planet {planet_id} not found"}, 404))
    #potentially thinking of making a loop to go through each PLANET in planetS
    return planet


# UPDATE ONE ENDPOINT
@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_planet(planet_id)

    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.color = request_body["color"]

    db.session.commit()

    return make_response(f"Planet {planet.id} successfully updated!"), 200

# DELETE ONE ENDPOINT
@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet {planet.id} successfully deleted!"), 200

# Reads all planets
@planets_bp.route("", methods=["GET"]) 
def read_all_planets():
        
        name_query = request.args.get("name")
        if name_query:
            planets = Planet.query.filter_by(name=name_query)
        else:
            planets = Planet.query.all()

            
        planets_response = []
        for planet in planets:
            planets_response.append(planet.to_dict())
        return jsonify(planets_response)

# GET ONE PLANET
@planets_bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = validate_planet(planet_id)
    return planet.to_dict(), 200

    
@planets_bp.route("", methods=["POST"]) # Validation for POST dictionary
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                description=request_body["description"],
                color=request_body["color"])

    
    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created.", 201)
    
# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except:
#         abort(make_response({"message":f"planet {planet_id} invalid"}, 400))
    
#     planet = Planet.query.get(planet_id)

#     if not planet:    
#         abort(make_response({"message":f"planet {planet_id} not found"}, 404))
    
#     return planet

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

