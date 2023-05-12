from app import db

class Planets():
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description
    
    def to_dict(self):
        planet_as_dict = {}
        planet_as_dict["id"] = self.id
        planet_as_dict["name"] = self.name
        planet_as_dict["description"] = self.description

        return planet_as_dict


# planets = [
#     Planets(1, "Saturn", "Gaseous planet with rings"),
#     Planets(2, "Jupiter", "Strom planet"),
#     Planets(3, "Venus", "Where girls come from")
# ]