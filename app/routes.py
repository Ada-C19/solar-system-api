from flask import Blueprint, jsonify, request, abort, make_response
from app import db
from app.models.planet import Planet

# class Planet:
#     def __init__(self, id, name, description, size):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.size = size

# mercury = Planet(1, "Mercury", "First planet from the sun", 3032)
# venus = Planet(2, "Venus", "Second planet from the sun", 7521)
# earth = Planet(3, "Earth", "Third planet from the sun", 7918)

# planet_list = [mercury, venus, earth]

planet_bp = Blueprint("planet", __name__, url_prefix="/planet")

@planet_bp.route("", methods=["POST"])
def add_planet():
    request_body = request.get_json()
    new_planet = Planet(name = request_body["name"], description = request_body["description"], size = request_body["size"])

    db.session.add(new_planet)
    db.session.commit()

    return {"id": new_planet.id}, 201

@planet_bp.route("", methods= ['GET'])
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

@planet_bp.route("/<id>", methods=["GET"])
def get_one_planet(id):
    planet = validate_planet(id)

    if planet is None: 
        return {"msg": f"id {id} not found"}, 404
    
    return planet.to_dict(), 200

def validate_planet(pl_id):
    try: 
        planet_id = int(pl_id)
    except ValueError:
        return abort(make_response({"msg": f"Invalid id: {pl_id}"}, 400))
    
    return Planet.query.get_or_404(planet_id, {"msg":"id not found"})

@planet_bp.route("/<id>", methods=["PUT"])
def update_planet(id):
    planet = validate_planet(id)

    request_data = request.get_json()

    planet.name = request_data["name"]
    planet.description = request_data["description"]
    planet.size = request_data["size"]

    db.session.commit()
    return {"msg": f"Planet {id} successfully updated"}, 200

@planet_bp.route("/<id>", methods=["DELETE"])
def delete_planet(id):
    planet = validate_planet(id)

    db.session.delete(planet)
    db.session.commit()

    return {"msg": f"Planet {id} successfully deleted"}, 200