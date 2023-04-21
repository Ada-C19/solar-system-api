from flask import Blueprint, jsonify, abort, make_response
import json

class Planet():

    def __init__(self, id, name, description, place):
        self.id = id 
        self.name = name 
        self.description = description
        self.place = place

Planets = [
    Planet(1, "Mercury", "filler", "First"),
    Planet(2, "Venus", "Filler", "Second"),
    Planet(3, "Earth", "Filler", "Third"),
    Planet(4, "Mars", "Filler", "Forth"),
    Planet(5, "Jupiter", "Filler", "Fifth"),
    Planet(6, "Saturn", "Filler", "Sixth"),
    Planet(7, "Uranus", "Filler", "Seventh"),
    Planet(8, "Neptune", "Filler", "Eighth")
]


planets = Blueprint ("planets", __name__, url_prefix="/planets")

@planets.route("", methods=["GET"])

def return_planets():
    planet_list = []

    for planet in Planets:
        planet_dict = {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "place": planet.place
        }
        planet_list.append(planet_dict)


    planets_json = json.dumps(planet_list)
    return planets_json



#...to get all existing planets, 
# so that I can see a list of planets, 
# with their id, name, description, 
# and other data of the planet.