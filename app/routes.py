from flask import Blueprint

solar_system_bp = Blueprint('solar_system', __name__)


@solar_system_bp.route('/solar_system', methods=['GET'])

def get_solar_system():
    return {"name": "Solar System"}