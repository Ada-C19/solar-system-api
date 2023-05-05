from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String)
    radius = db.Column(db.Integer)
    description = db.Column(db.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "radius": self.radius,
            "description": self.description
        }
    
    @classmethod 
    def from_dict(cls, planet_data):
        return cls(
            name = planet_data["name"],
            radius = planet_data["radius"],
            description = planet_data["description"],
        )

