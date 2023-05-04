from app import create_app, db
from app.models.planet import Planet

my_app = create_app()
with my_app.app_context():
    db.session.add(Planet(1, "Mercury", "hot", "grey")) 
    db.session.add(Planet(2, "Venus", "Planet of love", "orange")) 
    db.session.add(Planet(3, "Earth", "Home", "blue-green"))
    db.session.add(Planet(4, "Mars", "volatile", "red"))
    db.session.add(Planet(5, "Jupiter", "stormy", "beige"))
    db.session.add(Planet(6, "Saturn", "the rings", "yellow"))
    db.session.add(Planet(7, "Uranus", "the single ring", "light blue")) 
    db.session.add(Planet(8, "Neptune", "far away", "blue"))
    db.session.commit()