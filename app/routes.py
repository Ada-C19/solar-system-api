from flask import Blueprint,jsonify

class Planet: 
    def __init__(self, id, name, description, moons):
        id = self.id
        name = self.name
        description = self.description
        moons = self.moons 

    
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


