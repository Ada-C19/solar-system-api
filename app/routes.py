from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request

bp = Blueprint("planets", __name__, url_prefix="/planets")

@bp.route("", methods=["GET"])
def read_all_planets():
    planets = Planet.query.all()
    planets_response = []
    for planet in planets:
        planets_response.append(planet.make_planet_dict())
    return jsonify(planets_response)

@bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                    description=request_body["description"],
                    position=request_body["position"]
                    )

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201) 

@bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = validate_planet(planet_id)

    return jsonify(planet.make_planet_dict()), 200

@bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_planet(planet_id)
    request_body = request.get_json()

    planet.name=request_body["name"],
    planet.description=request_body["description"],
    planet.position=request_body["position"]
    
    db.session.commit()

    return make_response(f"Planet {planet.name} successfully updated", 200)

@bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
  planet = validate_planet(planet_id)

  db.session.delete(planet)
  db.session.commit()

  return make_response(f"Planet {planet.name} successfully deleted", 200)

# helper function
def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"Planet {planet_id} invalid"}, 400))

    planet = Planet.query.get(planet_id)
    
    if not planet:
        abort(make_response({"message":f"Planet {planet_id} not found"}, 404))
        
    return planet

# class Planet:
#     def __init__(self, id, name, description, position):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.position = position

# planets = [
#     Planet(1, ),
#     Planet(2, "Venus", "The hottest planet of the Solar System", "#2"), 
#     Planet(3, "Earth", "Seventy percent of its surface is cover with water", "#3"), 
#     Planet(4, "Mars", "Known as Red Planet because of iron oxide on its surface", "#4"),
#     Planet(5, "Jupiter", "The largest of the solar system, it's 2.5 times larger than all the other planets combined", "#5"), 
#     Planet(6, "Saturn", "Known as a gas giant with seven ring systems surrounding it", "#6"),
#     Planet(7, "Uranus", "It is the coldest planet of the Solar System with temperatures at around -224 degrees Celsius", "#7"),
#     Planet(8, "Neptune", "Has the fasted wind speeds of any planet, reaching speeds of 2.160 km / 1.314 mi per hour", "#8")
#     ]
