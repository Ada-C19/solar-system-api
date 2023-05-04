from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    type = db.Column(db.String)

    def to_dict(self):
        planet_as_dict = {}
        
        planet_as_dict["id"] = self.id
        planet_as_dict["name"] = self.name
        planet_as_dict["description"] = self.description
        planet_as_dict["type"] = self.type

        return planet_as_dict

    # def make_planet_dict(self):
    #     return dict(
    #         id=self.id,
    #         name=self.name,
    #         description=self.description,
    #         type=self.type
    #     )


