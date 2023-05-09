from flask import Blueprint, jsonify, request, make_response, abort
from app import db
from app.model.planets_model import Planet
from app.model.moon import Moon



planet_bp = Blueprint("planet", __name__, url_prefix="/planet")

#CREATE
@planet_bp.route("", methods=["POST"])
def add_planet():
    request_body = request.get_json()
    new_planet = Planet.from_dict(request_body)

    # new_planet = Planet(
    #     name = request_body['name'],
    #     description = request_body['description'],
    #     size = request_body['size']
    # )

    db.session.add(new_planet)
    db.session.commit()

    planet_dict = {
        "id": new_planet.id,
        "name": new_planet.name,
        "description": new_planet.description,
        "size": new_planet.size
    }

    return jsonify(planet_dict), 201




#GET ALL 
@planet_bp.route("", methods=["GET"])
def get_planets():
    response = []
    name_query = request.args.get("name")
    
    if name_query is None:
        all_planets = Planet.query.all()
    else:
        all_planets = Planet.query.filter_by(name=name_query)

    for planet in all_planets:
        response.append(planet.to_dict())
    return jsonify(response), 200


# GET ONE
@planet_bp.route("/<id>", methods=["GET"])
def get_one_planet(id):

    planet = validate_planet(Planet, id)

    return planet.to_dict(), 200


# GET UPDATE
@planet_bp.route("/<id>", methods=["PUT"])
def update_planet(id):

    planet = validate_planet(Planet,id)
    request_data = request.get_json()

    planet.name = request_data["name"]
    planet.description = request_data["description"]
    planet.size = request_data["size"]

    db.session.commit()

    return {"message": f"planet {id} has been updated"}, 200


# DELETE 
@planet_bp.route("/<id>", methods=["DELETE"])
def delete_planet(id):
    planet = validate_planet(Planet,id)

    db.session.delete(planet)
    db.session.commit()

    return {"message":f"planet {id} has been deleted"},200




# helper function
def validate_planet(model,planet_id):
    try:
        planet_id = int(planet_id)

    except ValueError:
        return abort(make_response({"message": f"invalide id {planet_id} not found"}, 400))

    return model.query.get_or_404(planet_id)
   

@planet_bp.route("/<planet_id>/moon", methods = ["POST"])
def add_moon_to_planet(id):
    planet = validate_planet(Planet,id)
    request_body = request.get_json()
    moon = Moon.from_dict(request_body)
    moon.planet = planet

    db.session.add(moon)
    db.session.commit()

    return jsonify({"msg": f"created moon with {planet.id}."})