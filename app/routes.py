from flask import Blueprint

class Planet:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

mercury = Planet(1, "Mercury", "smallest planet, and hot")
venus = Planet(2, "Venus", "small, the hottest")
earth = Planet(3, "Earth", "medium, green, lush, home planet, in danger")
mars = Planet(4, "Mars", "red, no water, also in danger")
jupiter = Planet(5, "Jupiter", "largest, many moons")
saturn = Planet(6, "Saturn", "cool rings, large")
uranus = Planet(8, "Uranus", "large, funny name")
neptune = Planet(7, "Neptune", "large, blue, cold")
pluto = Planet(8, "Pluto", "dwarf planet, very cold")

planet_list = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, pluto]