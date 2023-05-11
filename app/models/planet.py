from app import db
from flask import make_response, jsonify, abort

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    diameter = db.Column(db.Float)

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
            diameter=self.diameter
        )
    
    @classmethod
    def from_dict(cls, data):
        return Planet(
            name = data["name"],
            description = data["description"],
            diameter = data["diameter"]
        )
    
    @classmethod
    def validate_planet(cls, planet_id):
        try:
            planet_id = int(planet_id)
        except:
            abort(make_response(jsonify({"message": f"{cls.__name__} {planet_id} invalid"}), 400))

        planet = cls.query.get(planet_id)

        if not planet:
            abort(make_response(jsonify({"message": f"{cls.__name__} {planet_id} not found"}), 404))

        return planet