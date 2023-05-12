from app import db

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    
    
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