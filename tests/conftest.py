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
def multiple_planets(app):
    planet_1 = Planet(
        description="A dusty, cold, desert world with a very thin atmosphere",
        gravity="3.721 m/s²",
        habitable=False,
        id=1,
        moon_of_planet="Phobos & Deimos",
        name="Mars",
        nickname="Red Planet",
        size="6,792 km"
    )
    planet_2= Planet(
        name="Saturn",
        description="The second-largest planet in solar system.",
        size="36,183.7 miles",
        moon_of_planet="Iapetus, Rhea, Dione, and Tethys",
        habitable=False,
        id=2,
        gravity="10.44 m/s²",
        nickname="Ringed Planet"
    )
    planet_3 = Planet(
        name="Neptune",
        description="Dark, cold, and whipped by supersonic winds, ice giant.",
        size="24,622 km",
        moon_of_planet="Triton",
        habitable=False,
        id=3,
        gravity="11.15 m/s²",
        nickname="Ice Giant"
    )
    db.session.add_all([planet_1, planet_2, planet_3])
    db.session.commit()