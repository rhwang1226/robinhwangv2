from flask import Blueprint, render_template

# Initialize the Blueprint
views = Blueprint('views', __name__)

# Index route
@views.route('/')
def index():
    return render_template('index.html')

@views.route('/experience')
def experience():
    return render_template('experience.html')