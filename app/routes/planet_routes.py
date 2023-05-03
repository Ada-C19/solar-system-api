from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request, abort


planets_bp = Blueprint("planets", __name__, url_prefix="/planets")


# @planets_bp.route("", methods=["GET", "POST"])
# def handle_planetssss():
#     return make_response("I'm a teapot!", 418)

@planets_bp.route("", methods=["POST"])
def add_new_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body['name'],
                        description=request_body['description'],
                        moons=request_body['moons']
                        )

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

@planets_bp.route("", methods=["GET"])
def get_all_planets():
    planets = Planet.query.all()
    planets_list=[]
    for planet in planets:
        planets_list.append(planet.make_planet_dict())
    return jsonify(planets_list), 200

@planets_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet(planet_id):

    planet= validate_planet(planet_id)

    return planet.make_planet_dict()


@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet#{planet.id} successfully deleted")

@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet=validate_planet(planet_id)
    request_body=request.get_json()

    if request_body.get("name") is None or request_body.get("description") is None or request_body.get("moons") is None:
        return make_response(f"some additional information needed to update planet {planet.name}",400)

    planet.name=request_body["name"]
    planet.description=request_body["description"]
    planet.moons=request_body["moons"]

    db.session.commit()

    return make_response(f"planet {planet.name} succesfully updated",200)

def validate_planet(id):
    try:
        id = int(id)
    except:
        abort(make_response({"message":f"planet {id} invalid"}, 400))
    
    planet = Planet.query.get(id)
    
    if not planet:
        abort(make_response({"message":f"planet {id} not found"}, 404))
    return planet