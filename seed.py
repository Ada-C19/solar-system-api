from app import create_app, db
from app.models.planet import Planet

my_app = create_app()
with my_app.app_context():
    db.session.add(Planet(name="Mercury", description="dark gray", composition="terrestrial"))
    db.session.add(Planet(name="Venus", description="light yellow", composition="terrestrial"))
    db.session.add(Planet(name="Earth", description="blue and green", composition="terrestrial"))
    db.session.add(Planet(name="Mars", description="red", composition="terrestrial"))
    db.session.add(Planet(name="Jupiter", description="orange and brown", composition="gas giant"))

    db.session.commit()

