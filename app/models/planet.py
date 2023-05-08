from app import db


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    moons = db.relationship("Moon", back_populates="planet")

    @classmethod 
    def dict_to_model(cls, data_dict):
        return cls(name = data_dict["name"],
                description = data_dict["description"],
                moons = data_dict["moons"])

    def make_planet_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
            moons=self.moons
        )