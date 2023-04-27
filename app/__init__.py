from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app(test_config=None):
    app = Flask(__name__)
    
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:postgres@localhost:5432/solar_system_database"

    from .models.moon import Moon
    from .models.planet import Planet

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes.routes import solar_system_planet
    app.register_blueprint(solar_system_planet)

    from .routes.routes import solar_system_moon
    app.register_blueprint(solar_system_moon)

    return app
