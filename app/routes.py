from flask import Blueprint

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

#...to get all existing planets, 
# so that I can see a list of planets, 
# with their id, name, description, 
# and other data of the planet.