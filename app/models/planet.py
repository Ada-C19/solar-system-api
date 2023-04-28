from app import db

class Planet(db.Model):
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    name=db.Column(db.String, nullable=False)
    description=db.Column(db.String, nullable=False)
    solar_day=db.Column(db.Float, nullable=False)

    