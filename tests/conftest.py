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
def one_planet(app):
    planet = Planet(
        name = "Mars",
        description = "Planet of War",
        color = "Red"
    )

    db.session.add(planet)
    db.session.commit()

    return planet


@pytest.fixture
def get_all_planets(app):
    planets = [
        Planet(
            name="Venus", 
            description="Planet of love", 
            color="orange"
        ), 
        Planet(
            name="Earth", 
            description="Home", 
            color="blue-green"
        ),
    ]

    db.session.add_all(planets)
    db.session.commit()

    return planets

# @pytest.fixture
# def get_all_planets(app):
#     planets = [
#         Planet("Mercury", "hot", "grey"), 
#         Planet("Venus", "Planet of love", "orange"), 
#         Planet("Earth", "Home", "blue-green"),
#         Planet("Mars", "volatile", "red"), 
#         Planet("Jupiter", "stormy", "beige"), 
#         Planet("Saturn", "the rings", "yellow"), 
#         Planet("Uranus", "the single ring", "light blue"), 
#         Planet("Neptune", "far away", "blue") 
#     ]

#     db.session.add_all(planets)
#     db.session.commit()

#     return planets