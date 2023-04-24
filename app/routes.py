from flask import Blueprint, jsonify


class Planet:
    """Create class Planet"""

    def __init__(self, id, name, description, type):
        """Constructor with class attributes"""
        self.id = id
        self.name = name
        self.description = description
        self.type = type


# Create a list of instances of class Planet for each planet in our solar system.
planets = [
    Planet(1, "Mercury", "Smallest planet in the solar system. Its year is 88 days long. Closest to the Sun.", "Rocky/Terrestrial"),
    Planet(2, "Venus", "Hottest planet in the solar system. Has a thick, toxic atmosphere. Second planet from the Sun.", "Rocky/Terrestrial"),
    Planet(3, "Earth", "Water world rich with life. Third rock from the Sun.",
           "Rocky/Terrestrial"),
    Planet(4, "Mars", "Cold and desert-like; iron oxide makes it look red. Fourth planet from the Sun.", "Rocky/Terrestrial"),
    Planet(5, "Jupiter", "Largest planet in the solar system; home to the Great Red Spot. Fifth planet from the Sun.", "Gas giant"),
    Planet(6, "Saturn", "Known for its large and distinct planetary ring. Sixth planet from the Sun.", "Gas giant"),
    Planet(7, "Uranus", "Orbits on its side! Clouds of hydrogen sulfide makes it smell like rotten eggs. Seventh planet from the Sun.", "Ice giant"),
    Planet(8, "Neptune", "Coldest planet in the solar system; stormy and bright blue. Eighth planet from the Sun.", "Ice giant"),
]

# Instantiates a Blueprint
planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")


@planets_bp.route("", methods=["GET"])
def show_all_planets():
    """Response body in JSON format for a request to see all planetary information."""
    planets_response = []
    for planet in planets:
        planets_response.append(
            {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "type": planet.type,
            }
        )
    return jsonify(planets_response)


@planets_bp.route("/<planet_id>", methods=["GET"])
# Defines an endpoint that returns a response for one planet with its id, title, description, and type
def display_one_planet(planet_id):
    """Returns response body: dictionary literal for one planet with matching planet_id"""

    try:
        planet_id = int(planet_id)
    except:
        return {"message": f"planet {planet_id} invalid"}, 400

    for planet in planets:
        if planet.id == planet_id:
            return {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "type": planet.type
            }
    return {"message": f"planet {planet_id}, not found"}, 404
