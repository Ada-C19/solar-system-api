from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#create instances
db = SQLAlchemy()
migrate = Migrate()


def create_app(test_config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/solar_system_development'


    from.model.planets_model import Planet
    db.init_app(app)
    migrate.init_app(app, db)

    from .planets import planet_bp
    app.register_blueprint(planet_bp)

    return app
