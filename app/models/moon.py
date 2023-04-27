from app import db

class Moon(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String)
    radius = db.Column(db.Integer)
    planet_id = db.Column(db.Integer)

