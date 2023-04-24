from flask import Blueprint, jsonify, abort, make_response

class Planet:
    def __init__(self, id, name, description, diameter):
        self.id = id
        self.name = name
        self.description = description
        self.diameter = diameter
 
planets = [Planet(1, 'Venus', 'The hottest planet',12104 ),
           Planet(2,'Mercury', 'Has no natural satellite', 4879),
           Planet(3,'Earth', 'The only planet where life is found', 12742 )
     
 ]

planets_bp= Blueprint('planets', __name__,url_prefix='/planets')

@planets_bp.route("", methods=['GET'])

def handle_planets():
    planet_records= []
    for planet in planets:
        planet_records.append(
            {"id": planet.id,
              "name": planet.name,
              "description": planet.description,
              "diameter": planet.diameter}
        )
    return jsonify(planet_records)

def validate_planet(id):
    try:
        id = int(id)
    except:
        abort(make_response({"message": f" planet {id} invalid"}, 400))
    
    for planet in planets:
        if planet.id == id:
            return planet
    abort(make_response({"message":f"planet {id} not found"}, 404)) 
    
    
@planets_bp.route("/<planet_id>", methods= ['GET'])
def handle_book(planet_id):
    planet = validate_planet(planet_id)
    return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "diameter": planet.diameter
    }