from app import db
from app.models.Planet import Planet
from flask import Blueprint, jsonify, make_response, request

# class Planet():

#     def __init__(self, id, name, description, place):
#         self.id = id 
#         self.name = name 
#         self.description = description
#         self.place = place

# Planets = [
#     Planet(1, "Mercury", "filler", "First"),
#     Planet(2, "Venus", "Filler", "Second"),
#     Planet(3, "Earth", "Filler", "Third"),
#     Planet(4, "Mars", "Filler", "Forth"),
#     Planet(5, "Jupiter", "Filler", "Fifth"),
#     Planet(6, "Saturn", "Filler", "Sixth"),
#     Planet(7, "Uranus", "Filler", "Seventh"),
#     Planet(8, "Neptune", "Filler", "Eighth")
# ]


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

#to get all existing planets
#see a list of planets and their attributes
# def request_planets():
#     all_planets = Planets[id(name,description,place)]
#     return jsonify(all_planets)

# returns a dictionary
# def return_planets():
#     planet_list = []
    
#     for planet in Planets:
#         planet_dict = {
#             "id": planet.id,
#             "name": planet.name,
#             "description": planet.description,
#             "place": planet.place
#         }
#         planet_list.append(planet_dict)


#     planets_json = json.dumps(planet_list)
#     return planets_json



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
        
#             #return vars(planet), 200
#             # return jsonify({
#             #     "name" : planet.name
#             #     "id" :  planet.id
#             #     "description" : planet.description
#             #     "place" : planet.place
#             # })


