from flask import Blueprint, jsonify

class Planet():
    def __init__(self, id, name, radius, description):
        self.id = id 
        self.name = name 
        self.radius = radius
        self.description = description

class Moon():
    def __init__(self, id, name, radius, planet):
        self.id = id 
        self.name = name 
        self.radius = radius 
        self.planet = planet 

mercury = Planet(1, "mercury", 1516, "I am the smallest planet in our solar system")
venus = Planet(2, "venus", 3760, "I spin in the opposite direction from Earth")
earth = Planet(3, "earth", 6371, "I am the densest planet in our solar system")
mars = Planet(4, "mars", 2106, "I am the only planet humans sent rovers on")
jupiter = Planet(5, "jupiter", 43441, "I am more than twice as massive as all the other planets combined")
saturn = Planet(6, "saturn", 36184, "I am the one with the ring")
uranus = Planet(7, "uranus", 15759, "I am the coldest planet in the solar system")
neptune = Planet(8, "neptune", 15299, "I am the only planet in our solar system not visible to the naked eye")

planet_list = [mercury, venus, earth, mars]

moon = Moon(1, "moon", 1079, earth)
phobos = Moon(2, "phobos", 11, mars)
deimos = Moon(3, "deimos", 6.2, mars)
europa = Moon(4, "europa", 1560, mars)

moon_list = [moon, phobos, deimos, europa]

solar_system_planet = Blueprint("solar_system_planet", __name__, url_prefix="/solar_system/planet")


@solar_system_planet.route("", methods=["GET"])
def get_planets():
    return_list = []
    for planet in planet_list:
        return_list.append({
            "id": planet.id,
            "name": planet.name,
            "radius": planet.radius,
            "description": planet.description
        })
    return jsonify(return_list), 200

solar_system_moon = Blueprint("solar_system_moon", __name__, url_prefix="/solar_system/moon")

@solar_system_moon.route("", methods=["GET"])
def get_planets():
    return_list = []
    for moon in moon_list:
        return_list.append({
            "id": moon.id,
            "name": moon.name,
            "radius": moon.radius,
            "planet name": moon.planet.name
        })
    return jsonify(return_list), 200

