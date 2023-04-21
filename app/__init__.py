from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)

    from.routes import planets
    app.register_blueprint(planets)

    return app


