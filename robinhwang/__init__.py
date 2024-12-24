from flask import Flask
from .views import views

def create_app():
    app = Flask(__name__)

    # Register the views blueprint
    app.register_blueprint(views)

    return app
