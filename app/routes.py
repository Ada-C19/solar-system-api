from flask import Blueprint, jsonify, abort, make_response, request
from app.models.cat import Cat
from app import db

cats_bp = Blueprint("cats", __name__, url_prefix="/cats")

# POST /cats
@cats_bp.route("", methods=["POST"])
def create_cat():
    request_body = request.get_json()
    new_cat = Cat(
        name=request_body["name"],
        color=request_body["color"],
        personality=request_body["personality"],
    )

    db.session.add(new_cat)
    db.session.commit()

    message = f"Cat {new_cat.name} successfully created"
    return make_response(message, 201)

# GET /cats
@cats_bp.route("", methods=["GET"])
def get_all_cats():
    cats = Cat.query.all()
    results = []
    for cat in cats: 
        results.append(
            dict(
                id=cat.id, 
                name=cat.name, 
                color=cat.color, 
                personality=cat.personality
            )
        )

    return jsonify(results)








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