from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    size = db.Column(db.Integer)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "size": self.size
        }
    
    @classmethod
    def from_dict(cls, planet_data):
        return cls(
            name = planet_data["name"], 
            description = planet_data["description"], 
            size = planet_data["size"])