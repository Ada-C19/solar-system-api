from app import db

class Moon(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String)
    radius = db.Column(db.Integer)
    planet_id = db.Column(db.Integer)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "radius": self.radius,
            "planet_id": self.planet_id
        }
    
    @classmethod 
    def from_dict(cls, moon_data):
        return cls(
            name = moon_data["name"],
            radius = moon_data["radius"],
            planet_id = moon_data["planet_id"],
        )

