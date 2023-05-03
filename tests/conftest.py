import pytest
from app import create_app, db
from flask.signals import request_finished
from app.model.planets_model import Planet

@pytest.fixture
def app():
    app = create_app(testing= True)
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
def two_planets():
    plant_venus = Planet(name = "Venus",description = "this is Venus", size = 6666)
    plant_mars = Planet(name = "Mars",description = "this is Mars", size = 9999)

    db.session.add_all([plant_venus,plant_mars])
    db.session.commit()

        