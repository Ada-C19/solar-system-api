from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request , abort

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        message = f"{cls.__name__} {model_id} is invalid"
        abort(make_response({"message": message}, 400))

    model = cls.query.get(model_id)

    if not model:
        message = f"{cls.__name__} {model_id} not found"
        abort(make_response({"message": message}, 404))

    return model

@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    try:
        new_planet = Planet.from_dict(request_body)
        db.session.add(new_planet)
        db.session.commit()

        message = f"Planet {new_planet.name} successfully created"
        return make_response(jsonify(message), 201)
    
    except KeyError as e:
        abort(make_response({"message": f"missing required value: {e}"}, 400))

@planets_bp.route("", methods=["GET"])
def get_all_planets():
    name_query = request.args.get("name")
    nickname_query = request.args.get("nickname")
    if name_query:
        planets = Planet.query.filter_by(name = name_query)

    if nickname_query:
        planets = Planet.query.filter_by(nickname = nickname_query)

    planets = Planet.query.all()

    results= [planet.to_dict()for planet in planets]

    return jsonify(results)

@planets_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    return planet.to_dict()

@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet_to_update= validate_model(Planet, planet_id)
    planet_data= request.get_json()

    planet_to_update.name = planet_data["name"]
    planet_to_update.description = planet_data["description"]
    planet_to_update.size= planet_data["size"]
    planet_to_update.moon_of_planet = planet_data["moon_of_planet"]
    planet_to_update.habitable = planet_data["habitable"]
    planet_to_update.gravity = planet_data["gravity"]
    planet_to_update.nickname = planet_data["nickname"]

    db.session.commit()

    return make_response(jsonify(f"Planet { planet_to_update.name} updated"), 200)

@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet_to_delete = validate_model(Planet, planet_id)

    db.session.delete(planet_to_delete)
    db.session.commit()

    return make_response(jsonify(f"Planet {planet_to_delete.name} successfully deleted"), 200)
