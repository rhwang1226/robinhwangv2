from flask import Blueprint, render_template
import sqlite3
from datetime import datetime
import pytz

blogandphilosophy_views = Blueprint('blogandphilosophy', __name__)

DATABASE_PATH = "robinhwang/data/robinhwang.db"

def format_datetime(timestamp):
    """
    Converts a datetime string into a human-readable format and adjusts to Eastern Time (ET).
    Handles timestamps with and without fractional seconds.
    """
    try:
        # Try parsing with fractional seconds
        dt = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S.%f")
    except ValueError:
        # Fallback to parsing without fractional seconds
        dt = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
    
    # Assuming the input timestamp is in UTC, convert to ET
    utc = pytz.utc
    eastern = pytz.timezone("US/Eastern")
    dt = utc.localize(dt).astimezone(eastern)
    
    return dt.strftime("%B %d, %Y • %I:%M %p ET")


@blogandphilosophy_views.route('/blogandphilosophy', methods=['GET'])
def blogandphilosophy():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, title, content, visibility, created_at, updated_at, slug 
        FROM blog_posts
        WHERE visibility = 'public'
        ORDER BY created_at DESC
    """)
    posts = cursor.fetchall()
    conn.close()

    # Format the dates for each post
    formatted_posts = [
        (post[0], post[1], post[2], post[3],
         format_datetime(post[4]),  # Format created_at
         format_datetime(post[5]) if post[5] else None,
         post[6])  # Format updated_at (if exists)
        for post in posts
    ]

    conn.close()
    return render_template('blogandphilosophy.html', posts=formatted_posts)