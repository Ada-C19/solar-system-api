from flask import Blueprint, jsonify, request, abort, make_response
from app import db
from app.models.planet import Planet

planet_bp = Blueprint("planet", __name__, url_prefix="/planet")

@planet_bp.route("", methods=["POST"])
def add_planet():
    request_body = request.get_json()
    new_planet = Planet.from_dict(request_body)

    db.session.add(new_planet)
    db.session.commit()

    return {"id": new_planet.id}, 201

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

@planet_bp.route("/<p_id>", methods=["GET"])
def get_one_planet(p_id):
    planet = validate_item(Planet, p_id)

    return planet.to_dict(), 200


def validate_item(model, item_id):
    try:
        item_id = int(item_id)
    except ValueError:
        return abort(make_response({"message": f"invalid id: {item_id}"}, 400))
    
    return model.query.get_or_404(item_id)

@planet_bp.route("/<p_id>", methods=["PUT"])
def update_planet(p_id):
    planet = validate_item(Planet, p_id)

    request_data = request.get_json()

    planet.name = request_data["name"]
    planet.description = request_data["description"]
    planet.num_moons = request_data["num_moons"]

    db.session.commit()

    return {"msg": f"planet {p_id} successfully updated"}, 200

@planet_bp.route("/<p_id>", methods=["DELETE"])
def delete_planet(p_id):
    planet = validate_item(Planet, p_id)

    db.session.delete(planet)

    db.session.commit()

    return {"msg": f"planet {p_id} successfully deleted"}, 200
