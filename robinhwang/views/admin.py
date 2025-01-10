from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from functools import wraps
import sqlite3

admin_views = Blueprint('admin', __name__)

DB_PATH = 'robinhwang/data/robinhwang.db'

# Decorator to check login status
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('authenticated'):
            flash('You must be logged in to access this page.', 'danger')
            return redirect(url_for('login.login'))
        return f(*args, **kwargs)
    return decorated_function

@admin_views.route('/admin')
@login_required
def admin():
    """
    Admin dashboard page.
    """
    return render_template('admin.html')

# Route to add a new experience
@admin_views.route('/admin/add_relevant_experience', methods=['GET', 'POST'])
@login_required
def add_relevant_experience():
    """
    Handles adding a new experience to the database.
    """
    if request.method == 'POST':
        title = request.form['title']
        company = request.form['company']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        location = request.form['location']
        description = request.form['description']

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO relevant_experience (title, company, start_date, end_date, location, description)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (title, company, start_date, end_date, location, description))
        conn.commit()
        conn.close()

        flash('Experience added successfully!', 'success')
        return redirect(url_for('admin.edit_relevant_experiences'))

    return render_template('add_relevant_experience.html')

def get_all_relevant_experiences():
    """
    Fetch all experiences from the database in descending order (newest first).
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, title, company, start_date, end_date, location, description
        FROM relevant_experience
        ORDER BY id DESC
    """)
    experiences = cursor.fetchall()
    conn.close()
    return experiences

def get_relevant_experience_by_id(exp_id):
    """
    Fetch a specific experience by ID.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, company, start_date, end_date, location, description FROM relevant_experience WHERE id = ?", (exp_id,))
    experience = cursor.fetchone()
    conn.close()
    return experience

@admin_views.route('/admin/edit_relevant_experiences', methods=['GET'])
@login_required
def edit_relevant_experiences():
    """
    Displays all experiences with options to edit each one.
    """
    experiences = get_all_relevant_experiences()
    return render_template('edit_relevant_experience.html', experiences=experiences)

@admin_views.route('/admin/edit_relevant_experience/<int:exp_id>', methods=['GET', 'POST'])
@login_required
def edit_relevant_experience(exp_id):
    """
    Handles editing of a specific experience.
    """
    if request.method == 'POST':
        title = request.form['title']
        company = request.form['company']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        location = request.form['location']
        description = request.form['description']

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE relevant_experience
            SET title = ?, company = ?, start_date = ?, end_date = ?, location = ?, description = ?
            WHERE id = ?
        """, (title, company, start_date, end_date, location, description, exp_id))
        conn.commit()
        conn.close()

        flash('Experience updated successfully!', 'success')
        return redirect(url_for('admin.edit_relevant_experiences'))

    # Fetch experience data for the edit form
    experience = get_relevant_experience_by_id(exp_id)
    if not experience:
        flash('Experience not found!', 'danger')
        return redirect(url_for('admin.edit_relevant_experiences'))

    return render_template('edit_relevant_experience_form.html', experience=experience)

@admin_views.route('/admin/delete_relevant_experience/<int:exp_id>', methods=['POST'])
@login_required
def delete_relevant_experience(exp_id):
    """
    Handles deleting a specific experience by ID.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM relevant_experience WHERE id = ?", (exp_id,))
    conn.commit()
    conn.close()

    flash('Experience deleted successfully!', 'success')
    return redirect(url_for('admin.edit_relevant_experiences'))


####################################### COURSEWORK ##############################################

# Fetch all coursework
def get_all_coursework():
    """
    Fetch all coursework from the database in descending order (newest first).
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, title, institution, start_date, end_date, description
        FROM coursework
        ORDER BY id DESC
    """)
    coursework = cursor.fetchall()
    conn.close()
    return coursework

# Fetch a specific course by ID
def get_course_by_id(course_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, institution, start_date, end_date, description FROM coursework WHERE id = ?", (course_id,))
    course = cursor.fetchone()
    conn.close()
    return course

# Route to display all coursework
@admin_views.route('/admin/edit_coursework', methods=['GET'])
@login_required
def edit_coursework():
    coursework = get_all_coursework()
    return render_template('edit_coursework.html', coursework=coursework)

# Route to add new coursework
@admin_views.route('/admin/add_coursework', methods=['GET', 'POST'])
@login_required
def add_course():
    if request.method == 'POST':
        title = request.form['title']
        institution = request.form['institution']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        description = request.form['description']

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO coursework (title, institution, start_date, end_date, description)
            VALUES (?, ?, ?, ?, ?)
        """, (title, institution, start_date, end_date, description))
        conn.commit()
        conn.close()

        flash('Coursework added successfully!', 'success')
        return redirect(url_for('admin.edit_coursework'))

    return render_template('add_coursework.html')

# Route to edit existing coursework
@admin_views.route('/admin/edit_course/<int:course_id>', methods=['GET', 'POST'])
@login_required
def edit_course(course_id):
    if request.method == 'POST':
        title = request.form['title']
        institution = request.form['institution']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        description = request.form['description']

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE coursework
            SET title = ?, institution = ?, start_date = ?, end_date = ?, description = ?
            WHERE id = ?
        """, (title, institution, start_date, end_date, description, course_id))
        conn.commit()
        conn.close()

        flash('Coursework updated successfully!', 'success')
        return redirect(url_for('admin.edit_coursework'))

    course = get_course_by_id(course_id)
    if not course:
        flash('Course not found!', 'danger')
        return redirect(url_for('admin.edit_coursework'))

    return render_template('edit_course_form.html', course=course)

# Route to delete coursework
@admin_views.route('/admin/delete_course/<int:course_id>', methods=['POST'])
@login_required
def delete_course(course_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM coursework WHERE id = ?", (course_id,))
    conn.commit()
    conn.close()

    flash('Coursework deleted successfully!', 'success')
    return redirect(url_for('admin.edit_coursework'))
