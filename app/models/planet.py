from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    size = db.Column(db.String, nullable=False)
    moon_of_planet = db.Column(db.String, nullable=True)
    habitable = db.Column(db.Boolean)
    gravity = db.Column(db.String)
    nickname = db.Column(db.String, nullable=True)

    def to_dict(self):
        return dict(
            name=self.name,
            description=self.description,
            size=self.size,
            moon_of_planet=self.moon_of_planet,
            habitable=self.habitable,
            id=self.id,
            gravity=self.gravity,
            nickname=self.nickname
            )

    @classmethod
    def from_dict(cls, planet_data):
        return  cls(
            name = planet_data["name"],
            description = planet_data["description"],
            size = planet_data["size"],
            moon_of_planet = planet_data["moon_of_planet"],
            habitable = planet_data["habitable"],
            gravity = planet_data["gravity"],
            nickname = planet_data["nickname"]
        )
