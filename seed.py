from app import create_app, db
from app.models.planet import Planet

my_app = create_app()
with my_app.app_context():
    db.session.add(Planet(id="1", name="Apple Planet", description="A planet that only grows apples.", rating="5"))
    db.session.add(Planet(id="2", name="Orange Planet", description="A planet that only grows oranges.", rating="3"))
    db.session.add(Planet(id="3", name="Pear Planet", description="A planet that only grows pears.", rating="1"))
    db.session.commit()

    
