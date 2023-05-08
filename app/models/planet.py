from app import db
from flask import abort, make_response


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    association = db.Column(db.String)

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
            association=self.association,
            )
    
    @classmethod
    def from_dict(cls, planet_data):
        try:
            new_planet = Planet(name=planet_data["name"],
                                description=planet_data["description"],
                                association=planet_data["association"],
                                )
        except KeyError: 
            abort(make_response({"message": f"Provided planet data was invalid"}, 400))
        
        return new_planet

    def update_from_dict(self, planet_data):
        try:
            self.name = planet_data["name"]
            self.description = planet_data["description"]
            self.association = planet_data["association"]
        except KeyError: 
            abort(make_response({"message": f"Provided planet data was invalid"}, 400))