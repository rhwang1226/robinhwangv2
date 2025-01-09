import os
import sqlite3
from flask import Blueprint, render_template
from datetime import datetime

# Initialize Blueprint for educationandexperience
educationandexperience_views = Blueprint('educationandexperience', __name__)

# Path to the database
DATABASE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'robinhwang.db')

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

# Function to fetch leadership data from the database
def get_leadership_experience():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT title, role, year, description, image_path FROM conference_management_experience')
    leadership_experiences = cursor.fetchall()
    conn.close()
    return leadership_experiences

def get_licenses_and_certifications():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT title, issuer, issue_date, expiration_date, icon_path FROM licenses_and_certifications')
    licenses = cursor.fetchall()
    conn.close()
    return licenses

def get_other_experience():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT title, company, start_date, end_date, location, description FROM other_experience')
    other_experiences = cursor.fetchall()
    conn.close()
    return other_experiences


@educationandexperience_views.route('/educationandexperience')
def educationandexperience():
    # Fetch data from all tables
    relevant_experiences = get_relevant_experience()
    coursework = get_coursework()
    leadership_experiences = get_leadership_experience()
    licenses_and_certifications = get_licenses_and_certifications()
    other_experiences = get_other_experience()
    
    # Render the template with the data
    return render_template(
        'educationandexperience.html', 
        relevant_experiences=relevant_experiences,
        coursework=coursework,
        leadership_experiences=leadership_experiences,
        licenses_and_certifications=licenses_and_certifications,
        other_experiences=other_experiences
    )
