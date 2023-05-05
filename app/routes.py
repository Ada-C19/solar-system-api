from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.planet import Planet

# class Planet():
#     def __init__(self, id, name, description, distance_from_sun):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.distance_from_sun = distance_from_sun

# planet_list = [
#     Planet(1, "Mercury", "blue", 0.39),
#     Planet(2, "Venus", "yellow", 0.72),
#     Planet(3, "Earth", "blue", 1),
#     Planet(4, "Mars", "orange", 1.52),
#     Planet(5, "Jupiter", "orange", 5.2),
#     Planet(6, "Saturn", "yellow", 9.54),
#     Planet(7, "Uranus", "blue", 19.2),
#     Planet(8, "Neptune", "blue", 30.06)
# ]

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({'msg': f"Invalid id '{planet_id}'"}, 400))

    planet = Planet.query.get(planet_id)

    if planet:
        return planet
    else: 
        return abort(make_response({'msg': f"No planet with id {planet_id}"}, 404))



planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=['POST'])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                        description=request_body["description"],
                        distance_from_sun=request_body["distance from sun"])
    
    db.session.add(new_planet)
    db.session.commit()

    return ({
            "id": new_planet.id,
            "name": new_planet.name,
            "description": new_planet.description,
            "distance from sun": new_planet.distance_from_sun,
            "msg": "Successfully created"
        }, 201)

    # return make_response(f"Planet {new_planet.name} successfully created", 201)

@planets_bp.route("", methods=['GET'])
def get_planets():
    name_query = request.args.get("name")
    if name_query:
        planets = Planet.query.filter_by(name=name_query)
    else:
        planets = Planet.query.all()

    planets_response = []
    for planet in planets:
        planets_response.append(planet.to_dict())
    
    return jsonify(planets_response), 200


@planets_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet(planet_id):

    planet = validate_planet(planet_id)

    return ({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "distance from sun": planet.distance_from_sun
        }), 200


@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_one_planet(planet_id):
    # Get the data from the request body
    request_body = request.get_json()

    planet_to_update = validate_planet(planet_id)

    planet_to_update.name = request_body["name"]
    planet_to_update.description = request_body["description"]
    planet_to_update.distance_from_sun = request_body["distance from sun"]

    db.session.commit()

    return ({
            "id": planet_to_update.id,
            "name": planet_to_update.name,
            "description": planet_to_update.description,
            "distance from sun": planet_to_update.distance_from_sun
        }), 200



@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_one_planet(planet_id):
    planet_to_delete = validate_planet(planet_id)

    db.session.delete(planet_to_delete)
    db.session.commit()

    return f"Planet {planet_to_delete.name} is deleted!", 200


