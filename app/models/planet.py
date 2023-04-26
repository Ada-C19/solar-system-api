from app import db

class Planet(db.Model):
    id = db.Column(db.Integer,primary_key = True, autoincrement = True)
    name = db.Column(db.String)
    description = db.Column(db.Text)
    form = db.Column(db.String)