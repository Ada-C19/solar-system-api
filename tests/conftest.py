import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.planet import Planet


# CREATE A NEW "TEST" APP 
@pytest.fixture 
def app():
    app = create_app({"TESTING": True})

    # CLOSE THE DATABASE SESSION
    @request_finished.connect_via(app)
    def expire_session(send, response, **extra):
        db.session.remove()

    # AKA ARRANGE PORTION OF TESTING 
    # SET UP A DATABASE
    with app.app_context():
        db.create_all()  # RUN ALL THE MIGRATIONS
        yield app

    # CLEAR DATABASE
    with app.app_context():
        db.drop_all()

# CREATE A NEW CLIENT TO SEND OUR REQUESTS
# AKA: creating a pytest version of Postman
@pytest.fixture 
def client(app):
    return app.test_client()

@pytest.fixture
def two_planets(app):
    planet_one = Planet(id=1, name="Furby", description="Purple", distance_from_sun=17)
    planet_two = Planet(id=2, name="Squiggles", description="Orange", distance_from_sun=29)

    db.session.add(planet_one)
    db.session.add(planet_two)


    db.session.commit()


    # we are working on writing tests portion of wave 6 of project. We need to create fixtures and unit tests