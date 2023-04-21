# Define a Planet class with the attributes id, name, 
# and description, and one additional attribute

class Planet:
    def __init__(self, id, name, description, solar_day):
        self.id = id
        self.name = name
        self.description = description
        self.solar_day = solar_day 


planets = [
    Planet(1, "Mercury", "smallest planet", 176.0),
    Planet(2, "Venus", "planet of love", 243.0),
    Planet(3, "Earth", "home planet", 1.0),
    Planet(4, "Mars", "red planet", 1.25),
    Planet(5, "Jupiter", "largest planet", 0.42),
    Planet(6, "Saturn", "ring planet", .45),
    Planet(7, "Uranus", "coldest planet", .71),
    Planet(8, "Neptune", "not visible to the naked eye", .67),
    Planet(9, "Pluto", "unqualified planet", 6.375)
    ]