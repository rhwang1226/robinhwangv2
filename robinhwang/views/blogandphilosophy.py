from flask import Blueprint, render_template
import sqlite3
from datetime import datetime

blogandphilosophy_views = Blueprint('blogandphilosophy', __name__)

DATABASE_PATH = "robinhwang/data/robinhwang.db"

# Function to fetch blog entries sorted by most recent date
def get_blog_entries():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT title, content, date_posted FROM blog_entries ORDER BY date_posted DESC')
    blog_entries = cursor.fetchall()
    conn.close()
    
    # Convert date_posted to "Month Day, Year" format
    blog_entries = [(title, content, datetime.strptime(date_posted, '%Y-%m-%d').strftime('%B %d, %Y'))
                    for title, content, date_posted in blog_entries]
    
    return blog_entries

@blogandphilosophy_views.route('/blogandphilosophy')
def blogandphilosophy():
    blog_entries = get_blog_entries()
    return render_template('blogandphilosophy.html', blog_entries=blog_entries)