from flask import Blueprint,jsonify,abort, make_response

class Planet: 
    def __init__(self, id, name, description, moons):
        self.id = id
        self.name = name
        self.description = description
        self.moons = moons 

    
planets = [
    Planet(1, "Earth", "our planet", 1),
    Planet(2, "Mars", "red", 2)
]

bp= Blueprint ("planets", __name__, url_prefix="/planets")

@bp.route( "", methods=["GET"])

def get_list_of_planets(): 
    results_list= []

    for planet in planets: 
        results_list.append (dict(
            id =  planet.id,
            name = planet.name,
            description = planet.description,
            moons = planet.moons,

        ))
    
    return jsonify(results_list)
"""
@bp.route("/<id>",methods=["GET"])
def get_one_planet(id):
    id = validate_planet(id)
    
    for planet in planets:
        if id == planet.id:
            return {
                "id" : planet.id,
                "name" : planet.name,
                "description" : planet.description,
                "moons" : planet.moons 
            }
    
    abort(make_response({"message”:f”planet {id} not found"}, 404))

def validate_planet(id):
    try:
        id = int(id)
    except:
        abort(make_response({"message”:f”planet {id} invalid"}, 400))

    return id
"""
@bp.route("/<id>",methods=["GET"])
def get_one_planet(id):
    planet = validate_planet(id)
    return {
            "id" : planet.id,
            "name" : planet.name,
            "description" : planet.description,
            "moons" : planet.moons 
            }
    

def validate_planet(id):
    try:
        id = int(id)
    except:
        abort(make_response({"message": f"planet {id} invalid"}, 400))

    for planet in planets:
        if planet.id == id:
            return planet
    
    abort(make_response({"message": f"planet {id} not found"}, 404))
