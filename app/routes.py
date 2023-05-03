from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request, abort


'''Considering keeping the hard-coded planet info until such time as my
Postman is working.  If Gabby can test and find them working, I'm okay
with getting rid of the hard-coded info.  I'm just not sure how to test'''


# class Planet:
#     def __init__(self, id, name, description, distance_from_the_sun):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.distance_from_the_sun = distance_from_the_sun
#         # distance from the sun measured in AU--Astronmical Units


# planets = [
#     Planet(1, "Mercury", "The smallest planet; pitted and streaky, brownish-gray", 0.39),
#     Planet(2, "Venus", "A fireball with temperatures hot enough to melt lead, covered in thick clouds", 0.72),
#     Planet(3, "Earth", "A beautiful blue-green planet with life-supporting atmosphere", 1.00),
#     Planet(4, "Mars", "A rust-colored, dusty, cold, desert planet with a very thin atmosphere", 1.52),
#     Planet(5, "Jupiter", "A peachy-pearl gas giant with mass of more than twice the other planets combined", 5.20),
#     Planet(6, "Saturn", "A yellowish gas giant with rings made of ice and rock", 9.54),
#     Planet(7, "Uranus", "A blue-green gas giant which also has a ring system", 19.19),
#     Planet(8, "Neptune", "A blue gas giant with a stormy center and its own ring system", 30.06),
# ]

planets_bp = Blueprint('planets', __name__, url_prefix='/planets')

# helper functions
def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"Planet with id {planet_id} is invalid"}, 400))

    planet = Planet.query.get(planet_id)

    if not planet:
        abort(make_response({"message": f"Planet with id {planet_id} was not found"}, 404))

    return planet

# route functions
@planets_bp.route("", methods=["GET"])
def read_all_planets():
    name_query = request.args.get("name")
  
    if name_query:
        planets = Planet.query.filter_by(name=name_query)
    else:
        planets = Planet.query.all()

    planets_response = [planet.to_dict() for planet in planets]

    return jsonify(planets_response)

@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                        description=request_body["description"],
                        distance_from_the_sun=request_body["distance_from_the_sun"])
    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)
 
@planets_bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = validate_planet(planet_id)

    return planet.to_dict()

@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_planet(planet_id)

    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.distance_from_the_sun = request_body["distance_from_the_sun"]

    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully updated")

@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully deleted")

  