from app import db
from flask import make_response 

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    color = db.Column(db.String)
    # __tablename__ = "planets"

    
    def update(id, planet_to_dict):
        for key, value in planet_to_dict.items():
            setattr(id,key,value)
        
    
    def planet_to_dict(self):
        return {
        "id": self.id,
        "name": self.name,
        "description": self.description,
        "color": self.color }
    
    @classmethod 
    def create_new_planet(cls, request_data):
        if "name" not in request_data or "description" not in request_data:
            return make_response("Invalid Requesrt", 400)
        return cls(
            name=request_data["name"].title(),
            description=request_data["description"],
            color=request_data.get("color") 
        )
    
    def update(id, planet_to_dict):
        for key, value in planet_to_dict.items():
            setattr(id,key,value)

    def to_string(self):
        return f"{self.id}: {self.name} Description {self.description} "
    
    