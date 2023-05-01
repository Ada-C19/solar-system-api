from app import db
from app.models.Planet import Planet
from flask import Blueprint, jsonify, make_response, request


planets = Blueprint("planets", __name__, url_prefix="/planets")

@planets.route("", methods=["POST"])
def handle_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                    description=request_body["description"],
                    place=request_body["place"])
    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} succesfully created",201)


@planets.route("", methods=["GET"])
def return_all_planets():

    planets= Planet.query.all()
    planet_response = []

    for planet in planets:
        planet_response.append({
            "id": planet.id,
            "name": planet.name,
            "description":planet.description,
            'place':planet.place
        })
    return jsonify(planet_response)


@planets.route("/<planet_id>", methods=["GET"])
def returns_one_planet_info(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        return {"message":f"planet {planet_id} invalid"}, 400
    for planet in Planets:
        if int(planet_id) == planet.id:
            return vars(planet), 200
    return {"message":f"planet {planet_id} not found"}, 404


