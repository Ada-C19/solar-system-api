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
def two_saved_planets(app):
    # Arrange
    test_blue_planet = Planet(name="Blueto",
                    description="Watr 4evr",
                    position="#100")
    test_purple_planet = Planet(name="Purpley",
                    description="Ice 4evr",
                    position="#70")

    db.session.add_all([test_blue_planet, test_purple_planet])
    db.session.commit()
