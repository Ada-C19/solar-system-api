from flask import Blueprint, jsonify, abort, make_response

class Planet:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description 
    
    def make_planet_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
        )

planets = [
    Planet(1, "Apple Planet", "A planet that only grows Apple"),
    Planet(2, "Orange Planet", "A planet that only grows orange"),
    Planet(3, "Pear Planet", "A planet that only grows pear")
]

bp = Blueprint("planets", __name__, url_prefix="/planets")

def validate_planet(id):
    try:
        id = int(id)
    except:
        return abort(make_response({"message": f"{id} was invalid"}, 400))
    
    for planet in planets:
        if planet.id == id:
            return planet 
    return abort(make_response({"message": f"Cat with id {id} was not found"}, 404))


@bp.route("", methods=["GET"])

def get_all_planets():
    result_list = []

    for planet in planets:
        result_list.append(planet.make_planet_dict())

    return jsonify(result_list)


@bp.route("/<id>", methods=["GET"])
def search_single_planet(id):
    planet = validate_planet(id)

    return planet.make_planet_dict()

