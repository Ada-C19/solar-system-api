from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request

bp = Blueprint("planets", __name__, url_prefix="/planets")

# VALIDATE PLANET HELPER FUNCTIONS
def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message":f"{cls.__name__} {model_id} invalid"}, 400))

    model = cls.query.get(model_id)
    
    if not model:
        abort(make_response({"message":f"{cls.__name__} {model_id} not found"}, 404))

    return model

# CREATE A PLANET
@bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet.from_dict(request_body)

    db.session.add(new_planet)
    db.session.commit()

    return make_response(jsonify(f"Planet {new_planet.name} successfully created")), 201


# READ ALL PLANETS
@bp.route("", methods=["GET"])
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


# READ ONE PLANET 
@bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    return planet.to_dict()

# UPDATE ONE PLANET
@bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    request_body = request.get_json()

    planet.name=request_body["name"],
    planet.description=request_body["description"],
    planet.position=request_body["position"]
    
    db.session.commit()

    return make_response(jsonify(f"Planet {update_planet.name} successfully updated"))

# DELETE A PLANET
@bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(jsonify(f"Planet {planet.name} successfully deleted"))

