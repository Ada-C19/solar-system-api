from app import db

class Moon(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    planet= db.relationship("Planet", back_populates="moons")
    planet_id= db.Column(db.Integer, db.ForeignKey('planet.id'))

    @classmethod 
    def dict_to_model(cls, data_dict):
        return cls(name = data_dict["name"])
    
    def make_moon_dict(self):
        return dict(
            name=self.name
        )