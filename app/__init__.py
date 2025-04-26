from flask import Flask, Blueprint
from config import Config
from app.extensions import db, migrate
from .routes import register_routes

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Register blueprints

    register_routes(app)
    # Register the main blueprint


    
    return app