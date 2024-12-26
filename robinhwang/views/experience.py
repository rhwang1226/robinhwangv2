import os
import sqlite3
from flask import Blueprint, render_template

# Initialize Blueprint for experience
experience_views = Blueprint('experience', __name__)

# Path to the database
DATABASE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'experience.db')

# Function to fetch relevant experience data from the database
def get_relevant_experience():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT title, company, start_date, end_date, location, description FROM relevant_experience')
    experiences = cursor.fetchall()
    conn.close()
    return experiences

# Function to fetch coursework data from the database
def get_coursework():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT title, institution, start_date, end_date, description FROM coursework')
    coursework = cursor.fetchall()
    conn.close()
    return coursework

@experience_views.route('/experience')
def experience():
    # Fetch data from both tables
    relevant_experiences = get_relevant_experience()
    coursework = get_coursework()
    return render_template(
        'experience.html', 
        relevant_experiences=relevant_experiences, 
        coursework=coursework
    )
