from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request, Response


# class Planet:
#     def __init__(self, id, name, description):
#         self.id = id
#         self.name = name
#         self.description = description

# planets = [
#     Planet(1, "Mercury", "Terrestrial planet closest to the sun. Smallest planet."),
#     Planet(2, "Venus", "Terrestrial planet second from sun. Hot surface."),
#     Planet(3, "Earth", "Third planet from the sun. Largest terrestrial planet."),
#     Planet(4, "Mars", "Terrestrial planet fourth from the sun. Red planet."),
#     Planet(5, "Jupiter", "First gas giant planet from the sun. Largest planet."),
#     Planet(6, "Saturn", "Sixth planet from the sun. Gas giant planet with rings."),
#     Planet(7, "Uranus", "Seventh planet from the sun. Ice giant planet."),
#     Planet(8, "Neptune", "Furthest planet from the sun. Cold, blue gas giant planet.")
# ]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET", "POST"])
def handle_planets():
    if request.method == "GET":
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

        return make_response(f"Planet {new_planet.name} successfully created", 201)


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

# @planets_bp.route("", methods=["POST"])
# def create_planet():
#     request_body = request.get_json()
#     new_planet = Planet(name=request_body["name"],
#                         description=request_body["description"])

#     db.session.add(new_planet)
#     db.session.commit()

#     return make_response(f"Planet {new_planet.name} successfully created", 201)