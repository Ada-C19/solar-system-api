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
    nebula = Planet(
        name="Nebula",
        description="Fake planet for testing purposes",
        solar_day=420.0
    )

    gamora = Planet(
        name="Gamora",
        description="Do not visit. Not a real place.",
        solar_day=666.0
    )

    db.session.add_all([nebula, gamora])
    db.session.commit()

@pytest.fixture
def walla_walla():
    return {
        "name": "Walla-Walla",
        "description": "A bad place.",
        "solar_day": 0.5
        }