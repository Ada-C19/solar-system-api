from flask import Blueprint, jsonify

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