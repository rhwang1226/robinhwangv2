import os
import sqlite3
from flask import Blueprint, render_template
from datetime import datetime

# Initialize Blueprint for educationandexperience
educationandexperience_views = Blueprint('educationandexperience', __name__)

@educationandexperience_views.route('/educationandexperience')
def educationandexperience():
    return render_template('educationandexperience.html')
