from flask import Blueprint, jsonify, abort, make_response, request
from app.models.planet import Planet
from app import db

planets_bp = Blueprint('planets', __name__, url_prefix='/planets')

@planets_bp.route("", methods=['POST'])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(
        name = request_body["name"],
        description = request_body["description"],
        mass = request_body["mass"],
    )

    db.session.add(new_planet)
    db.session.commit()

    message = f"New planet {new_planet.name} successfully created, biatch!"

    return make_response(message, 201)

@planets_bp.route("", methods=["GET"])
def get_planets():
    mass = request.args.get("mass")

    planets = Planet.query

    if mass:
        planets = planets.filter_by(mass=mass)

    planets = planets.all()

    request_body = []
    for planet in planets:
        request_body.append(
            dict(
                id=planet.id,
                name=planet.name,
                description=planet.description,
                mass=planet.mass
            )
        )
    return jsonify(request_body), 200

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"Planet {planet_id} is invalid, sucker!"}, 400))
    
    planet = Planet.query.get(planet_id)

    if not planet:
        abort(make_response({"message": f"Planet {planet_id} was not found, sucker!"}, 404))

    return planet

@planets_bp.route("/<planet_id>", methods=['GET'])
def read_one_planet(planet_id):
    planet = validate_planet(planet_id)
    return {         
        "id" : planet.id,   
        "name": planet.name,
        "description": planet.description,
        "mass": planet.mass
        }

@planets_bp.route("/<planet_id>", methods=['PUT'])
def update_planet(planet_id):
        planet = validate_planet(planet_id)
        request_body = request.get_json()
            
        planet.name = request_body["name"]
        planet.description = request_body["description"]
        planet.mass = request_body["mass"]

        db.session.commit()

        message = f"Planet {planet} succesfully updated, biatch!"

        return make_response({"message": message}, 200)

@planets_bp.route("/<planet_id>", methods=['DELETE'])
def delete_planet(planet_id):
        planet = validate_planet(planet_id)

        db.session.delete(planet)
        db.session.commit()

        message = f"Planet {planet} succesfully deleted, biatch!"

        return make_response({"message": message}, 200)



