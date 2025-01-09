import sqlite3
from flask import Blueprint, render_template

projects_views = Blueprint('projects', __name__)

DATABASE_PATH = "robinhwang/data/robinhwang.db"

# Function to fetch project data
def get_projects():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT title, description, technologies, github_link FROM projects')
    projects = cursor.fetchall()
    conn.close()
    return projects

@projects_views.route('/projects')
def projects():
    project_data = get_projects()
    return render_template('projects.html', projects=project_data)
