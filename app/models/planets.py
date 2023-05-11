from app import db

class Planets(db.Model):
    id = int
    name = "Saturn"
    description = "big planet"