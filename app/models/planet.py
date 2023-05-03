
from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    distance_from_the_sun = db.Column(db.Float)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "distance_from_the_sun": self.distance_from_the_sun
        }
     
    @classmethod
    def from_dict(cls, planet_data):
        return Planet(name=planet_data["name"],
                      description=planet_data["description"],
                      distance_from_the_sun=planet_data["distance_from_the_sun"])