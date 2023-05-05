from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    @classmethod
    def from_dict(cls, data_dict):
        return cls(
            id=data_dict["id"],
            name=data_dict["name"],
            description=data_dict["description"],
            rating=data_dict["rating"]
        )
    
    def to_dictionary(self):
        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
            rating=self.rating
        )
