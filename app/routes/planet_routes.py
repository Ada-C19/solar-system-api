from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response,request

bp = Blueprint("planets", __name__, url_prefix="/planets")

@bp.route("", methods= ["GET"])
def handle_planet():
    planets = Planet.query.all()
    planets_list = []
    for planet in planets:
        planets_list.append(planet.make_planet_dict())

    return jsonify(planets_list), 200

@bp.route("", methods= ["POST"])
def create_planet():
    request_body= request.get_json() 

    new_planet= Planet(
        name= request_body["name"]
        description= request_body["description"]
        orbital_period= request_body["orbital_period"]
    )

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Book {new_planet} successfully created", 201)