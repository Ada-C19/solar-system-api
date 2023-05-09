from app import db 
from app.models.moon import Moon 
from app.models.planet import Planet 
from flask import Blueprint, jsonify, abort, make_response, request

moons_bp = Blueprint("moons_bp", __name__, url_prefix="/moons")

# CREATE ENDPOINT
@moons_bp.route("", methods = ["POST"])
def create_moon():
    request_body = request.get_json()

    new_moon = Moon(name = request_body["name"])

    db.session.add(new_moon)
    db.session.commit()

    return make_response(f"caretaker {new_moon.name} successfully created", 201)

# SHOW ALL ENDPOINT
@moons_bp.route("", methods = ["GET"])
def handle_moons():
    moon_query = Moon.query.all()

    moon_response = []

    for moon in moon_query:
        moon_response.append({"name": moon.name})

    return jsonify(moon_response)

