from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request


planets_bp = Blueprint("books", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def add_new_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                        description=request_body["description"],
                        moons=request_body["moons"]
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