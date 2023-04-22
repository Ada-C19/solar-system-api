from flask import Blueprint, jsonify, abort, make_response, request    

class Planet:
    def __init__(self, id, name, description, distance_from_the_sun): 
        self.id = id
        self.name = name
        self.description = description
        self.distance_from_the_sun = distance_from_the_sun
        #distance from the sun measured in AU--Astronmical Units

planets = [
    Planet(1, "Mercury", "The smallest planet; pitted and streaky, brownish-gray", 0.39),
    Planet(2, "Venus", "A fireball with temperatures hot enough to melt lead, covered in thick clouds", 0.72),
    Planet(3, "Earth", "A beautiful blue-green planet with life-supporting atmosphere", 1.00),
    Planet(4, "Mars", "A rust-colored, dusty, cold, desert planet with a very thin atmosphere", 1.52),
    Planet(5, "Jupiter", "A peachy-pearl gas giant with mass of more than twice the other planets combined", 5.20),
    Planet(6, "Saturn", "A yellowish gas giant with rings made of ice and rock", 9.54),
    Planet(7, "Uranus", "A blue-green gas giant which also has a ring system", 19.19),
    Planet(8, "Neptune", "A blue gas giant with a stormy center and its own ring system", 30.06),
]
solar_system_bp = Blueprint('solar_system', __name__)
planets_bp = Blueprint('planets', __name__, url_prefix='/planets')

def validate_planet(planet_id):
    #handle invalid  planet_id, return 400
    try: 
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"Planet with id {planet_id} is invalid"}, 400))
    
    #search for planet_id in planets
    for planet in planets:
        if planet.id == planet_id:
            return planet
        
    #if planet_id not found, return 404
    abort(make_response({"message": f"Planet with id {planet_id} was not found"}, 404))


@solar_system_bp.route('/solar_system', methods=['GET'])
@planets_bp.route("", methods=['GET'])

def handle_planets():
    planets_response = []
    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "distance_from_the_sun": planet.distance_from_the_sun,  
        })
    return jsonify(planets_response)

@planets_bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):
    planet = validate_planet(planet_id)


    return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "distance_from_the_sun": planet.distance_from_the_sun,
    }

def get_solar_system():
    return {"name": "Solar System"}