from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    composition = db.Column(db.String)

    @classmethod
    def from_dict(cls, data_dict):
        return cls(
            name=data_dict["name"],
            description=data_dict["description"],
            composition=data_dict["composition"]
        )

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
            composition=self.composition
        )