import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.Planet import Planet


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
    #Arrange
    venus= Planet (name="Venus",description ="Gassy love goddess", place= 2)
    earth = Planet(name="Earth",description ="le home", place= 3)
    
    db.session.add_all([venus,earth])
    db.session.commit()


