import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.planet import Planet


@pytest.fixture
def app():
    app = create_app({'TESTING': True})

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
def two_saved_planets(app):
    mercury = Planet(name="Mercury",
                     description="The smallest planet; pitted and streaky, brownish-gray",
                     distance_from_the_sun=0.39)

    venus = Planet(name="Venus",
                   description="A fireball with temperatures hot enough to melt lead, covered in thick clouds",
                   distance_from_the_sun=0.72)

    db.session.add_all([mercury, venus])

    db.session.commit()
