from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    color = db.Column(db.String)
    moon = db.relationship("Moons", back_populates="planet")

    @classmethod
    def from_dict(cls, planet_data):
        new_planet = cls(
                    name = planet_data["name"],
                    description = planet_data["description"],
                    color = planet_data["color"]
                    )   
        return new_planet

    def make_planet_dict(self):
        planet_dict = dict (
            id = self.id,
            name = self.name,
            description = self.description,
            color = self.color 
        )
        return planet_dict
