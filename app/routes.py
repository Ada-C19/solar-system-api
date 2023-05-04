from flask import Blueprint, jsonify, abort, make_response, request
from app.models.planet import Planet
from app import db

# class Planet:
#     def __init__(self, id, name, description, diameter):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.diameter = diameter
 
# planets = [Planet(1, 'Venus', 'The hottest planet',12104 ),
#            Planet(2,'Mercury', 'Has no natural satellite', 4879),
#            Planet(3,'Earth', 'The only planet where life is found', 12742 )
     
#  ]

planets_bp= Blueprint('planets', __name__,url_prefix='/planets')
# Helper function
def validate_planet(cls,model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message": f" {cls.__name__} {model_id} invalid"}, 400))
    
    model = cls.query.get(model_id)
    if not model:
        abort(make_response({"message":f"{cls.__name__} {model_id} not found"}, 404))
    return model
    
     
    
# Routes
@planets_bp.route("", methods=['POST'])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet.from_dict(request_body)
    db.session.add(new_planet)
    db.session.commit()
    return make_response(jsonify(f"Planet {new_planet.name} was created successfully"), 201)

@planets_bp.route("", methods=['GET'])

def read_all_planets():
    name_query = request.args.get("name")
    if name_query:
        planets = Planet.query.filter_by(name=name_query)
    else:
        planets = Planet.query.all()
    planet_records= []
    for planet in planets:
        planet_records.append(
            planet.to_dict())
    return jsonify(planet_records)
    
    
@planets_bp.route("/<planet_id>", methods= ['GET'])
def get_one_planet(planet_id):
    planet = validate_planet(Planet, planet_id)
    
    return planet.to_dict()
    
    
@planets_bp.route("/<planet_id>", methods= ['PUT'])
def update_planet(planet_id):
    planet = validate_planet(Planet, planet_id)
    request_body = request.get_json()
    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.form = request_body["form"]
    
    db.session.commit()
    return make_response(jsonify(f"Planet {planet_id} updated succesffuly"), 200)

@planets_bp.route("/<planet_id>", methods= ['DELETE'])
def delete_planet(planet_id):
    planet = validate_planet(Planet, planet_id)
    db.session.delete(planet)
    db.session.commit()
    return make_response(jsonify(f"Planet {planet_id} deleted successfully"))