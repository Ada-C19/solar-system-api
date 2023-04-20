from flask import Blueprint

class Planet():

    def __init__(self, id, name, description, place):
        self.id = id 
        self.name = name 
        self.description = description
        self.place = place

Mercury = Planet(1, "Mercury", "filler", "First")
Venus = Planet(2, "Venus", "Filler", "Second")
Earth = Planet (3, "Earth", "Filler", "Third")
Mars = Planet(4, "Mars", "Filler", "Forth")
Jupiter = Planet (5, "Jupiter", "Filler", "Fifth")
Saturn= Planet (6, "Saturn", "Filler", "Sixth")
Uranus= Planet (7, "Uranus", "Filler", "Seventh")
Neptune = Planet(8, "Neptune", "Filler", "Eighth")

