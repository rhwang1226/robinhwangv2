from flask import Blueprint, render_template

projects_views = Blueprint('projects', __name__)

@projects_views.route('/projects')
def projects():
    return render_template('projects.html')