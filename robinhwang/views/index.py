from flask import Blueprint, render_template

index_views = Blueprint('index', __name__)

@index_views.route('/')
def index():
    return render_template('index.html')