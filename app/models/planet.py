from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    distance = db.Column(db.String(255), nullable=False)
    moons = db.relationship("Moon", back_populates="planet")

    def to_dict(self):
        moon_data = []
        if self.moons:
            for moon in self.moons:
                moon_data.append(moon.to_dict())
            
            
        
        return ({"id": self.id,
                "name": self.name,
                "description": self.description,
                "distance": self.distance,
                "moons" : moon_data})
    
    @classmethod
    def from_dict(cls, data_dict):
        return cls(
            name = data_dict["name"],
            description = data_dict["description"],
            distance = data_dict["distance"]
        )