from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    distance_from_sun = db.Column(db.Integer)


    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "distance from sun": self.distance_from_sun
        }

    @classmethod
    def from_dict(cls, planet_details):
        new_planet = cls(
            name=planet_details["name"],
            description=planet_details["description"],
            distance_from_sun=planet_details["distance from sun"]
        )
        return new_planet

