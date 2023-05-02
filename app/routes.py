from flask import Blueprint, jsonify, abort, make_response, request
from app.models.planet import Planet
from app import db

planets_bp = Blueprint('planets', __name__, url_prefix='/planets')

@planets_bp.route("", methods=['POST'])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(
        name = request_body["name"],
        description = request_body["description"],
        mass = request_body["mass"],
        # moons = request_body["moons"],
        # distance_from_sun = request_body["distance_from_sun"],
        # surface_area = request_body["surface_area"],
        # namesake = request_body["namesake"],
        # visited_by_humans = request_body['visited_by_humans'],
    )

    db.session.add(new_planet)
    db.session.commit()

    message = f"New planet {new_planet.name} successfully created!"
    return make_response(message, 201)

@planets_bp.route("", methods=["GET"])
def get_planets():
    planets = planets.all()
    request_body = []
    for planet in planets:
        request_body.append(
            dict(
                id=planet.id,
                name=planet.name,
                description=planet.description,
                mass=planet.mass,
                # moons=planet.moons,
                # distance_from_sun=planet.distance_from_sun,
                # surface_area=planet.surface_area,
                # namesake=planet.namesake,
                # visited_by_humans=planet.visited_by_humans,
            )
        )
    return jsonify(request_body), 200








# from flask import Blueprint, jsonify, abort, make_response

# class Planet:
#     def __init__(self, id, name, description, mass):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.mass = mass

#     def to_dict(self):
#         return dict(
#             id = self.id, 
#             name = self.name, 
#             description = self.description, 
#             mass = self.mass
#         )
        
# planet_list = [
#     Planet(1, "Mercury", "Small, rocky planet closest to the Sun", 0.330),
#     Planet(2, "Venus", "Hottest planet in the solar system with a thick atmosphere", 4.87),
#     Planet(3, "Earth", "Home to a diverse range of life forms, including humans", 5.97),
#     Planet(4, "Mars", "Red planet with a thin atmosphere and polar ice caps", 0.642),
#     Planet(5, "Jupiter", "Largest planet in the solar system with a thick atmosphere and many moons", 1898),
#     Planet(6, "Saturn", "Known for its prominent rings made of ice and dust", 568),
#     Planet(7, "Uranus", "Blue-green planet with a tilted axis of rotation", 86.8),
#     Planet(8, "Neptune", "Blue planet with a windy atmosphere and many storms", 102),
# ]

# planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

# @planets_bp.route("", methods=["GET"])
# def get_planets():
#     planets_response = []
#     for planet in planet_list:
#         planets_response.append(planet.to_dict())

#     return jsonify(planets_response), 200

# @planets_bp.route("/<id>", methods=["GET"])
# def get_planet(id):
#     planet = validate_planet(id)

#     return planet.to_dict()

# def validate_planet(id):
#     try:
#         id = int(id)
    
#     except:
#         abort(make_response({"message": f"Planet {id} is invalid!"}, 400))
    
#     for planet in planet_list:
#         if planet.id == id:
#             return planet

#     abort(make_response({"message": f"Planet {id} is not found!"}, 404))