from app import db

class Planet(db.Model):
    id = db.Column(db.Integer,primary_key = True, autoincrement = True)
    name = db.Column(db.String)
    description = db.Column(db.Text)
    form = db.Column(db.String)
    
    def to_dict(self):
        planet_dict = {}
        planet_dict["id"] = self.id
        planet_dict["name"] = self.name
        planet_dict["description"] = self.description
        planet_dict["form"] = self.form
        
        return planet_dict
    @classmethod
    def from_dict(cls, planet_data):
        new_planet = Planet(name=planet_data["name"],
                            description=planet_data["description"],
                            form=planet_data["form"])
        return new_planet