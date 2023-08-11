import pytest
from app import create_app, db
from flask.signals import request_finished
from app.models.moon import Moon 
from app.models.planet import Planet

@pytest.fixture
def app():
    app = create_app(testing = True)

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app
    
    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture 
def two_planets(app):
    mercury = Planet(name="mercury", radius=1516, description="I am the smallest planet in our solar system")
    venus = Planet(name="venus", radius=3760, description="I spin in the opposite direction from Earth")
    
    db.session.add_all([mercury, venus])
    db.session.commit()

