from flask import Flask
from robinhwang.views.index import index_views
from robinhwang.views.experience import experience_views

def create_app():
    app = Flask(__name__)

    # Register Blueprints
    app.register_blueprint(index_views)
    app.register_blueprint(experience_views)

    return app
