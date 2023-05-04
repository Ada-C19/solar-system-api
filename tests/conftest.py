import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.planet import Planet

@pytest.fixture
def app():
    app = create_app({"TESTING" : True})
    
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
def saved_planets(app):
    planet_mercury = Planet(name = "Mercury", description = "rocky planet", form = "solid" )
    planet_venus = Planet(name = "Venus", description = "gassy planet", form = "gas" )
    db.session.add_all([planet_mercury, planet_venus])
    db.session.commit()
    