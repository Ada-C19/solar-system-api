from app import create_app, db
from app.models.planet import Planet

my_app = create_app()
with my_app.app_context():
    db.session.add(Planet(name = "Mercury", description = "hot", color = "grey")) 
    db.session.add(Planet(name = "Venus", description = "Planet of love", color = "orange")) 
    db.session.add(Planet(name = "Earth", description = "Home", color = "blue-green"))
    db.session.add(Planet(name = "Mars", description = "volatile", color = "red"))
    db.session.add(Planet(name = "Jupiter", description = "stormy", color = "beige"))
    db.session.add(Planet(name = "Saturn", description = "the rings", color = "yellow"))
    db.session.add(Planet(name = "Uranus", description = "the single ring", color = "light blue")) 
    db.session.add(Planet(name =  "Neptune", description = "far away", color = "blue"))
    db.session.commit()