from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")


def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response(jsonify({"message":f"planet {planet_id} invalid"}), 400))
    
    planet = Planet.query.get(planet_id)
    if not planet:
        abort(make_response(jsonify({"message":f"planet {planet_id} not found"}), 404))

    return planet



@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                        description=request_body["description"],
                        solar_day=request_body["solar_day"])
    db.session.add(new_planet)
    db.session.commit()

    return make_response(jsonify(f"Planet {new_planet.name} created successfully."), 201)

@planets_bp.route("", methods=["GET"])
def get_all_planets():
    planets = Planet.query.all()
    results = [planet.to_dict() for planet in planets]
    
    return jsonify(results)

@planets_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)

    return planet.to_dict()

@planets_bp.route("/<planet_id>", methods=["PUT"])
def replace_planet(planet_id):
    planet = validate_planet(planet_id)
    planet_to_update = request.get_json()
    planet.name = planet_to_update["name"]
    planet.description = planet_to_update["description"]
    planet.solar_day = planet_to_update["solar_day"]

    db.session.commit()

    return make_response(jsonify(f"Planet {planet.name} updated successfully."))


@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet_to_delete = validate_planet(planet_id)
    db.session.delete(planet_to_delete)
    db.session.commit()

    return make_response(jsonify(f"Planet {planet_to_delete.name} was deleted."))




# Define a Planet class with the attributes id, name, 
# and description, and one additional attribute

# class Planet:
#     def __init__(self, id, name, description, solar_day):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.solar_day = solar_day

#     def to_dict(self):
#         return dict(
#             id=self.id,
#             name=self.name,
#             description=self.description,
#             solar_day=self.solar_day
#         )

# planets = [
#     Planet(1, "Mercury", "smallest planet", 176.0),
#     Planet(2, "Venus", "planet of love", 243.0),
#     Planet(3, "Earth", "home planet", 1.0),
#     Planet(4, "Mars", "red planet", 1.25),
#     Planet(5, "Jupiter", "largest planet", 0.42),
#     Planet(6, "Saturn", "ring planet", .45),
#     Planet(7, "Uranus", "coldest planet", .71),
#     Planet(8, "Neptune", "not visible to the naked eye", .67),
#     Planet(9, "Pluto", "unqualified planet", 6.375)
#     ]

        # Wave 2
        # read one planet
        # return 400 for invalid id
        # return 404 for non existing planet

# @planets_bp.route("", methods=["GET"])  
# def handle_planets():
#     results = [planet.to_dict() for planet in planets]

#     return jsonify(results)

# @planets_bp.route("/<planet_id>", methods=["GET"])
# def handle_planet(planet_id):
#     planet = validate_planet(planet_id)

#     return planet.to_dict()


        

    