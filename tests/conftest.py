import pytest
from app import create_app, db
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
def one_planet(app):
    return {
        "name" : "test_name_1",
        "description" : "test_description_1",
        "mass" : 1.000}


@pytest.fixture
def get_planets(app):
    test_planet_2 = Planet(name = "test_name_2", description = "test_description_2", mass = 2.000)
    test_planet_3 = Planet(name = "test_name_3", description = "test_description_3", mass = 3.000)

    test_planets = [test_planet_2, test_planet_3]

    db.session.add_all(test_planets)
    db.session.commit()

    return test_planets