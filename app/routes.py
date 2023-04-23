from flask import Blueprint

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
    Planet(3, "Earth", "Water world rich with life. Third rock from the Sun.", "Rocky/Terrestrial"),
    Planet(4, "Mars", "Cold and desert-like; iron oxide makes it look red. Fourth planet from the Sun.", "Rocky/Terrestrial"),
    Planet(5, "Jupiter", "Largest planet in the solar system; home to the Great Red Spot. Fifth planet from the Sun.", "Gas giant"),
    Planet(6, "Saturn", "Known for its large and distinct planetary ring. Sixth planet from the Sun.", "Gas giant"),
    Planet(7, "Uranus", "Orbits on its side! Clouds of hydrogen sulfide makes it smell like rotten eggs. Seventh planet from the Sun.", "Ice giant"),
    Planet(8, "Neptune", "Coldest planet in the solar system; stormy and bright blue. Eighth planet from the Sun.", "Ice giant"),
]

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")