from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)
    
    from .routes import solar_system_planet
    app.register_blueprint(solar_system_planet)

    from .routes import solar_system_moon
    app.register_blueprint(solar_system_moon)

    return app
