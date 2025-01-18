from flask import Flask
from robinhwang.views.index import index_views
from robinhwang.views.educationandexperience import educationandexperience_views
from robinhwang.views.projects import projects_views
from robinhwang.views.blogandphilosophy import blogandphilosophy_views
from robinhwang.views.login import login_views
from robinhwang.views.admin import admin_views
import markdown

import os
from dotenv import load_dotenv

def create_app():
    app = Flask(__name__)
    
    load_dotenv()

    app.secret_key = os.getenv('SECRET_KEY')

    # Register Blueprints
    app.register_blueprint(index_views)
    app.register_blueprint(educationandexperience_views)
    app.register_blueprint(projects_views)
    app.register_blueprint(blogandphilosophy_views)
    app.register_blueprint(login_views)
    app.register_blueprint(admin_views)

    # Register Markdown filter
    @app.template_filter('markdown')
    def markdown_filter(content):
        return markdown.markdown(content, extensions=['fenced_code', 'tables'])

    return app

