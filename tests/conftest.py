# 1. Create a test to check `GET` `/planets` returns `200` and an empty array.
import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.planets import Planets


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
def create_one_planet():
    new_planet = Planets(name="Saturn",
                        description="Planet has rings.")
    
    db.session.add(new_planet)
    db.session.commit()

@pytest.fixture
def read_all_planets():
    saturn = Planets(name="Saturn",
                        description="Planet has rings.")
    jupiter = Planets(name="Jupiter",
                        description="Planet has storms the size of earth!")
    
    db.session.add_all([saturn, jupiter])
    db.session.commit()
