from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from dotenv import load_dotenv
import os

#create instances
db = SQLAlchemy()
migrate = Migrate()

load_dotenv()


def create_app(testing=None):
    app = Flask(__name__)

 # CHANGES

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if testing is None:

        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
            "SQLALCHEMY_DATABASE_URI")

    else:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "SQLALCHEMY_TEST_DATABASE_TEST")
    
    # app.config["DEBUG"] = True


    


    from .model.planets_model import Planet
    from .model.moon import Moon

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes.planets import planet_bp
    app.register_blueprint(planet_bp)

    from .routes.moons import moon_bp
    app.register_blueprint(moon_bp)

    return app
