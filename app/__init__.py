from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

db= SQLAlchemy()
migrate = Migrate()

load_dotenv()

def create_app(testing=None):
    app = Flask(__name__)
    
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    if testing is None:
        app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:postgres@localhost:5432/solar_system_development"
    else:
        app.config["SQLALCHEMY_TEST_DATABASE_URI"] = "postgresql+psycopg2://postgres:postgres@localhost:5432/solar_system_test"

    from .models.planet import Planet

    db.init_app(app)
    migrate.init_app(app, db)

    from.routes import planet_bp
    app.register_blueprint(planet_bp)
    return app
