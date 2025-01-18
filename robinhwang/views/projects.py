import psycopg2
from flask import Blueprint, render_template
import os

projects_views = Blueprint('projects', __name__)

DATABASE_URL = os.getenv("DATABASE_URL")

# Function to fetch project data
def get_projects():
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute('SELECT title, description, technologies, github_link FROM projects')
    projects = cursor.fetchall()
    conn.close()
    return projects

@projects_views.route('/projects')
def projects():
    project_data = get_projects()
    return render_template('projects.html', projects=project_data)
