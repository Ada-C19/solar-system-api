from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os 
from dotenv import load_dotenv

db = SQLAlchemy()
migrate = Migrate()

load_dotenv()


def create_app(testing=None):
    app = Flask(__name__)
    
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    if not testing:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("RENDER_DATABASE_URI")
    else: 
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_TEST_DATABASE_URI")

    from .models.moon import Moon
    from .models.planet import Planet

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes.routes import solar_system_planet
    app.register_blueprint(solar_system_planet)

    from .routes.routes import solar_system_moon
    app.register_blueprint(solar_system_moon)

    return app
