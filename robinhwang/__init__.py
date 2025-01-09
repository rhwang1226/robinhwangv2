from flask import Flask
from robinhwang.views.index import index_views
from robinhwang.views.educationandexperience import educationandexperience_views
from robinhwang.views.projects import projects_views
from robinhwang.views.blogandphilosophy import blogandphilosophy_views

def create_app():
    app = Flask(__name__)

    # Register Blueprints
    app.register_blueprint(index_views)
    app.register_blueprint(educationandexperience_views)
    app.register_blueprint(projects_views)
    app.register_blueprint(blogandphilosophy_views)

    return app
