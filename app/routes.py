from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.planet import Planet


planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

def validate_planet(planet_id):
    #handle invalid planet_id, return 400
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({ "message":f"planet {planet_id} invalid"}, 400))

    planet = Planet.query.get(planet_id)

    if not planet:
        abort(make_response({"message":f"planet {planet_id} not found"}, 404))

    #search for planet_in in data, return planet
    return planet

    
@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                        description=request_body["description"],
                        color=request_body["color"])
    
    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)


@planets_bp.route("", methods=["GET"])
def read_all_planets():
    color_query = request.args.get("color")

    if color_query:
        planets = Planet.query.filter_by(color=color_query)
    else:
        planets = Planet.query.all()

    planets_response = []
    for planet in planets:
        planets_response.append({
            "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "color": planet.color
        })

    return jsonify(planets_response), 200


@planets_bp.route("/<planet_id>", methods=["GET"])
def single_planet(planet_id):
    planet = validate_planet(planet_id)

    return {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "color": planet.color
            }

@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_planet(planet_id)

    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.color = request_body["color"]

    db.session.commit()

    return make_response(jsonify(f"Planet #{planet.id} successfully updated"))


@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully deleted")

