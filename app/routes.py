from flask import Blueprint

class Planet:
    def __init__(self, id, name, description, dista
    nce_from_the_sun): #distance from the sun measured in AU--Astronmical Units
        self.id = id
        self.name = name
        self.description = description
        self.distance_from_the_sun = distance_from_the_sun

solar_system_bp = Blueprint('solar_system', __name__)


@solar_system_bp.route('/solar_system', methods=['GET'])

def get_solar_system():
    return {"name": "Solar System"}