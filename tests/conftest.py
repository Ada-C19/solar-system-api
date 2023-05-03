import pytest
from app import create_app, db 
from flask.signals import request_finished
from app.models.planet import Planet

@pytest.fixture
def app():
    app = create_app(True)

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
    saturn = Planet(name="Saturn", description="the ringed planet", size=72367)
    uranus = Planet(name="Uranus", description="seventh planet from the Sun", size=31518)

    db.session.add_all([saturn, uranus])
    db.session.commit()
