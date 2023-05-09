from app import db
from app.models.planet import Planet
from app.models.moon import Moon 
from flask import Blueprint, jsonify, make_response, request, abort
from .routes_helpers import validate_model

moons_bp = Blueprint("moons", __name__, url_prefix="/moons")


@moons_bp.route("", methods=["POST"])
def make_new_moon():
    request_body = request.get_json()
    
    new_moon = Moon(name=request_body["name"])

    db.session.add(new_moon)
    db.session.commit()

    return make_response(f"Moon {new_moon.name} successfully created", 201)

@moons_bp.route("", methods=["GET"])
def get_all_moons():

    name_param = request.args.get("name")
    
    if name_param:
        moons = Moon.query.filter_by(name=name_param)
    else:
        moons = Moon.query.all()

    moons_list=[moon.make_moon_dict()for moon in moons]

    return jsonify(moons_list), 200