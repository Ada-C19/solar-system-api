from flask import Blueprint

class Planet:
    def __init__(self, id, name, description, color):
        self.id = id
        self.name = name
        self.description = description
        self.color = color

planets = [
    Planet(1, "Earth", "habitable", "blue & green"),
    Planet(2, "Venus", "hot", "yellowy orange"),
    Planet(3, "Saturn", "beautiful ringlets", "light yellow"),
    Planet(4, "Neptune", "furthest from the sun", "blue")
]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")