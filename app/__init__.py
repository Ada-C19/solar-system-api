from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/solar_system_development'

    db.init_app(app)
    migrate.init_app(app, db)

    from app.models.planet import Planet
    
    from app.routes import planets_bp
    app.register_blueprint(planets_bp)

    return app
