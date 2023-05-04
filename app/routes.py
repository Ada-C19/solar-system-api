from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request, Response

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET", "POST"])
def handle_planets():
    if request.method == "GET":

        name_query = request.args.get("name")
        if name_query:
            planets = Planet.query.filter_by(name=name_query)           
        else:
            planets = Planet.query.all()

        planets_response = []
        for planet in planets:
            planets_response.append({
                "id": planet.id,
                "name": planet.name,
                "description": planet.description
            })
        return jsonify(planets_response)
    
    elif request.method == "POST":
        request_body = request.get_json()
        new_planet = Planet(name=request_body["name"],
                            description=request_body["description"])

        db.session.add(new_planet)
        db.session.commit()

        return make_response(jsonify(f"Planet {new_planet.name} successfully created"), 201)


def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"planet {planet_id} invalid"}, 400))
    
    planet = Planet.query.get(planet_id)

    if not planet:
        abort(make_response({"message":f"planet {planet_id} not found"}, 404))

    return planet


@planets_bp.route("/<planet_id>", methods=["GET", "PUT", "DELETE"])
def handle_one_planet(planet_id):
    planet = validate_planet(planet_id)
    
    if request.method == "GET":
        return {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
        }

    elif request.method == "PUT":
        request_body = request.get_json()

        planet.name = request_body["name"]
        planet.description = request_body["description"]

        db.session.commit()

        return make_response(f"Planet #{planet.id} successfully updated")

    elif request.method == "DELETE":
        db.session.delete(planet)
        db.session.commit()

        return make_response(f"Planet #{planet.id} successfully deleted")
    