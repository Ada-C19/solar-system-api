from flask import Blueprint, jsonify, abort, make_response,request
from app.models.planet import Planet
from app import db

planet_bp = Blueprint("planets", __name__, url_prefix="/planets")

# POST /planets
@planet_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(
        name = request_body["name"],
        description = request_body["description"],
        distance_from_sun = request_body["distance_from_sun"],
    )
    
    db.session.add(new_planet)
    db.session.commit()
    
    message = f"Planet {new_planet.name} successfully created"
    return make_response(message, 201)


@planet_bp.route("", methods=["GET"])
def get_all_planets():
    planets = Planet.query.all()
    results = []
    for planet in planets:
        results.append(
            dict(
                id=planet.id,
                name=planet.name,
                description=planet.description,
                distance_from_sun=planet.distance_from_sun
            )
        )
    return jsonify(results)


# class Planet:
#     def __init__(self, id, name, description, distance_from_sun):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.distance_from_sun = distance_from_sun

#     def to_dict(self):
#         return dict(
#             id=self.id,
#             name=self.name,
#             description=self.description,
#             distance_from_sun=self.distance_from_sun
#         )


# planets = [Planet(1, "Mercury", "Mercury has zero moons", 3.5),
#            Planet(2, "Venus", "Venus has zero moons", 6.7),
#            Planet(3, "Earth", "Earth has one moon", 9.3),
#            Planet(4, "Mars", "Mars has two moons", 14.2),
#            Planet(5, "Jupiter", "Jupiter has sixty-seven moons", 48.4),
#            Planet(6, "Saturn", "Saturn has sixty-two moons", 88.9),
#            Planet(7, "Uranus", "Uranus has twenty-seven moons", 179),
#            Planet(8, "Neptune", "Neptune has fourteen moons", 288),
#            Planet(9, "Pluto", "Pluto has five moons", 367)
#            ]



# @planet_bp.route("", methods=["GET"])
# def get_all_planets():
#     all_planets_response = []
#     for planet in planets:
#         all_planets_response.append(planet.to_dict())

#     return jsonify(all_planets_response)


# @planet_bp.route("/<id>", methods=["GET"])
# def get_one_planet(id):
#     planet = validate_planet(id)

#     return planet.to_dict()


# def validate_planet(id):
#     try:
#         id = int(id)
#     except:
#         abort(make_response({"message": f"planet {id} is invalid"}, 400))

#     for planet in planets:
#         if planet.id == id:
#             return planet

#     abort(make_response({"message": f"planet {id} not found"}, 404))
