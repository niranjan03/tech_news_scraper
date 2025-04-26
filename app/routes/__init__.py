from flask import Blueprint
# from flask import request

# Create main blueprint
bp = Blueprint('main', __name__)

# Import all route modules
from . import api
from . import views

# Register blueprints
def register_routes(app):
    app.register_blueprint(bp)
    app.register_blueprint(api.bp, url_prefix='/api')
    app.register_blueprint(views.bp)