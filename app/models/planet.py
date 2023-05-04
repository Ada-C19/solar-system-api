from app import db

class Planet(db.Model):
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    name=db.Column(db.String, nullable=False)
    description=db.Column(db.String, nullable=False)
    solar_day=db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "solar_day": self.solar_day
        }
    
    @classmethod
    def from_dict(cls, planet_data):
        return Planet(
            name=planet_data["name"],
            description=planet_data["description"],
            solar_day=planet_data["solar_day"]
        )
