from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    position = db.Column(db.String)

    def to_dict(self):
        planet_as_dic = {}
        planet_as_dic["id"] = self.id
        planet_as_dic["name"] = self.name
        planet_as_dic["description"] = self.description
        planet_as_dic["position"] = self.position

        return planet_as_dic
    
    @classmethod
    def from_dict(cls, planet_data):
        new_planet = Planet(name=planet_data["name"],
                        description=planet_data["description"],
                        position=planet_data["position"])
        
        return new_planet
