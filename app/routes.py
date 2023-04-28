from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request

# planets = [
#     Planet(1, "Mercury", "smallest planet", "Wednesday"),
#     Planet(2, "Mars", "spicy, red one", "Tuesday"),
#     Planet(3, "Jupiter", "biggest planet", "Thursday"),
#     Planet(4, "Venus", "hottest planet", "Friday"),
#     Planet(5, "Saturn", "the one with the rings", "Saturday")
# ]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

# def validate_planet(id):
#     try:
#         id = int(id)
#     except ValueError:
#         abort(make_response({'message': f'Planet {id} is invalid.'}, 400))

#     for planet in planets:
#         if planet.id == id:
#              return planet
#     abort(make_response({'message': f'Planet {id} not found.'}, 404))

# @planets_bp.route("/<id>", methods=["GET"])
# def handle_planet(id):
#     planet = validate_planet(id)

#     return planet.make_planet_dict()


@planets_bp.route("", methods=["GET"])
def handle_planets():
    planets = Planet.query.all()

    planets_response = [Planet.make_planet_dict(planet) for planet in planets]

    return jsonify(planets_response)


@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                        description=request_body["description"],
                        association=request_body["association"])

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f'Planet {new_planet} successfully created.', 201)
