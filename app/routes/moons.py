from flask import Blueprint, jsonify, request, make_response, abort
from app import db
from app.model.moon import Moon
from app.model.planets_model import Planet




moon_bp = Blueprint("moon", __name__, url_prefix="/moon")

# CREATE
@moon_bp.route("", methods=["POST"])
def add_moon():
    request_body = request.get_json()
    new_moon = Moon.from_dict(request_body)

    db.session.add(new_moon)
    db.session.commit()

    # moon_dict = {
    #     "id": new_moon.moon_id,
    #     "name": new_moon.name
    # }

    return jsonify(
                    {new_moon.to_dict()}
                ), 201


# GET ALL
@moon_bp.route("", methods=["GET"])
def get_moons():
    response = []

    all_moons = Moon.query.all()

    for moon in all_moons:
        response.append(moon.to_dict())
        
    return jsonify(response), 200


# GET ONE
@moon_bp.route("/<moon_id>", methods=["GET"])
def get_one_moon(moon_id):

    moon = Moon.query.all(moon_id)

    return moon.to_dict(), 200

