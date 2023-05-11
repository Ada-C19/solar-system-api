import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.planet import Planet

@pytest.fixture
def app():
    app = create_app({"TESTING": True})

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
    planet_one = Planet(name="Planet1",
                        description="First planet",
                        diameter=5000)
    planet_two = Planet(name="Planet2",
                        description="Second planet",
                        diameter=7500)
    db.session.add_all([planet_one, planet_two])
    db.session.commit()