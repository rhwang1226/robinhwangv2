from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from functools import wraps
import psycopg2
from datetime import datetime
import pytz
import uuid
import os

admin_views = Blueprint('admin', __name__)

DATABASE_URL = os.getenv("DATABASE_URL")

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

        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO relevant_experience (title, company, start_date, end_date, location, description)
            VALUES (%s, %s, %s, %s, %s, %s)
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
    conn = psycopg2.connect(DATABASE_URL)
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
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, company, start_date, end_date, location, description FROM relevant_experience WHERE id = %s", (exp_id,))
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

        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE relevant_experience
            SET title = %s, company = %s, start_date = %s, end_date = %s, location = %s, description = %s
            WHERE id = %s
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
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM relevant_experience WHERE id = %s", (exp_id,))
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
    conn = psycopg2.connect(DATABASE_URL)
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
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, institution, start_date, end_date, description FROM coursework WHERE id = %s", (course_id,))
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

        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO coursework (title, institution, start_date, end_date, description)
            VALUES (%s, %s, %s, %s, %s)
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

        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE coursework
            SET title = %s, institution = %s, start_date = %s, end_date = %s, description = %s
            WHERE id = %s
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
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM coursework WHERE id = %s", (course_id,))
    conn.commit()
    conn.close()

    flash('Coursework deleted successfully!', 'success')
    return redirect(url_for('admin.edit_coursework'))

####################################### CONFERENCE MANAGEMENT ##############################################
# Fetch all conferences
def get_all_conferences():
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, role, year, description, image_path FROM conference_management_experience")
    conferences = cursor.fetchall()
    conn.close()
    return conferences

# Fetch a specific conference by ID
def get_conference_by_id(conference_id):
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, role, year, description, image_path FROM conference_management_experience WHERE id = %s", (conference_id,))
    conference = cursor.fetchone()
    conn.close()
    return conference

# Route to display all conferences
@admin_views.route('/admin/edit_conferences', methods=['GET'])
@login_required
def edit_conferences():
    conferences = get_all_conferences()
    return render_template('edit_conferences.html', conferences=conferences)

# Route to add a new conference
@admin_views.route('/admin/add_conference', methods=['GET', 'POST'])
@login_required
def add_conference():
    if request.method == 'POST':
        title = request.form['title']
        role = request.form['role']
        year = request.form['year']
        description = request.form['description']
        image_path = request.form['image_path']  # File path to the uploaded image.

        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO conference_management_experience (title, role, year, description, image_path)
            VALUES (%s, %s, %s, %s, %s)
        """, (title, role, year, description, image_path))
        conn.commit()
        conn.close()

        flash('Conference added successfully!', 'success')
        return redirect(url_for('admin.edit_conferences'))

    return render_template('add_conference.html')

# Route to edit an existing conference
@admin_views.route('/admin/edit_conference/<int:conference_id>', methods=['GET', 'POST'])
@login_required
def edit_conference(conference_id):
    if request.method == 'POST':
        title = request.form['title']
        role = request.form['role']
        year = request.form['year']
        description = request.form['description']
        image_path = request.form['image_path']

        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE conference_management_experience
            SET title = %s, role = %s, year = %s, description = %s, image_path = %s
            WHERE id = %s
        """, (title, role, year, description, image_path, conference_id))
        conn.commit()
        conn.close()

        flash('Conference updated successfully!', 'success')
        return redirect(url_for('admin.edit_conferences'))

    conference = get_conference_by_id(conference_id)
    if not conference:
        flash('Conference not found!', 'danger')
        return redirect(url_for('admin.edit_conferences'))

    return render_template('edit_conference_form.html', conference=conference)

# Route to delete a conference
@admin_views.route('/admin/delete_conference/<int:conference_id>', methods=['POST'])
@login_required
def delete_conference(conference_id):
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM conference_management_experience WHERE id = %s", (conference_id,))
    conn.commit()
    conn.close()

    flash('Conference deleted successfully!', 'success')
    return redirect(url_for('admin.edit_conferences'))

####################################### LICENSES AND CERTIFICATIONS ##############################################

# Fetch all licenses and certifications
def get_all_licenses_and_certifications():
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, issuer, issue_date, expiration_date, icon_path FROM licenses_and_certifications")
    licenses = cursor.fetchall()
    conn.close()
    return licenses

# Fetch a specific license or certification by ID
def get_license_by_id(license_id):
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, issuer, issue_date, expiration_date, icon_path FROM licenses_and_certifications WHERE id = %s", (license_id,))
    license = cursor.fetchone()
    conn.close()
    return license

# Route to display all licenses and certifications
@admin_views.route('/admin/edit_licenses', methods=['GET'])
@login_required
def edit_licenses():
    licenses = get_all_licenses_and_certifications()
    return render_template('edit_licenses.html', licenses=licenses)

# Route to add a new license or certification
@admin_views.route('/admin/add_license', methods=['GET', 'POST'])
@login_required
def add_license():
    if request.method == 'POST':
        title = request.form['title']
        issuer = request.form['issuer']
        issue_date = request.form['issue_date']
        expiration_date = request.form.get('expiration_date')  # Optional
        icon_path = request.form['icon_path']  # File path to the uploaded icon.

        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO licenses_and_certifications (title, issuer, issue_date, expiration_date, icon_path)
            VALUES (%s, %s, %s, %s, %s)
        """, (title, issuer, issue_date, expiration_date, icon_path))
        conn.commit()
        conn.close()

        flash('License or Certification added successfully!', 'success')
        return redirect(url_for('admin.edit_licenses'))

    return render_template('add_license.html')

# Route to edit an existing license or certification
@admin_views.route('/admin/edit_license/<int:license_id>', methods=['GET', 'POST'])
@login_required
def edit_license(license_id):
    if request.method == 'POST':
        title = request.form['title']
        issuer = request.form['issuer']
        issue_date = request.form['issue_date']
        expiration_date = request.form.get('expiration_date')  # Optional
        icon_path = request.form['icon_path']

        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE licenses_and_certifications
            SET title = %s, issuer = %s, issue_date = %s, expiration_date = %s, icon_path = %s
            WHERE id = %s
        """, (title, issuer, issue_date, expiration_date, icon_path, license_id))
        conn.commit()
        conn.close()

        flash('License or Certification updated successfully!', 'success')
        return redirect(url_for('admin.edit_licenses'))

    license = get_license_by_id(license_id)
    if not license:
        flash('License or Certification not found!', 'danger')
        return redirect(url_for('admin.edit_licenses'))

    return render_template('edit_license_form.html', license=license)

# Route to delete a license or certification
@admin_views.route('/admin/delete_license/<int:license_id>', methods=['POST'])
@login_required
def delete_license(license_id):
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM licenses_and_certifications WHERE id = %s", (license_id,))
    conn.commit()
    conn.close()

    flash('License or Certification deleted successfully!', 'success')
    return redirect(url_for('admin.edit_licenses'))

####################################### OTHER EXPERIENCES ##############################################

# Fetch all other experiences
def get_all_other_experiences():
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, company, start_date, end_date, location, description FROM other_experience")
    experiences = cursor.fetchall()
    conn.close()
    return experiences

# Fetch a specific other experience by ID
def get_other_experience_by_id(exp_id):
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, company, start_date, end_date, location, description FROM other_experience WHERE id = %s", (exp_id,))
    experience = cursor.fetchone()
    conn.close()
    return experience

# Route to display all other experiences
@admin_views.route('/admin/edit_other_experiences', methods=['GET'])
@login_required
def edit_other_experiences():
    experiences = get_all_other_experiences()
    return render_template('edit_other_experiences.html', experiences=experiences)

# Route to add a new other experience
@admin_views.route('/admin/add_other_experience', methods=['GET', 'POST'])
@login_required
def add_other_experience():
    if request.method == 'POST':
        title = request.form['title']
        company = request.form['company']
        start_date = request.form['start_date']
        end_date = request.form.get('end_date')  # Optional
        location = request.form['location']
        description = request.form['description']

        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO other_experience (title, company, start_date, end_date, location, description)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (title, company, start_date, end_date, location, description))
        conn.commit()
        conn.close()

        flash('Other Experience added successfully!', 'success')
        return redirect(url_for('admin.edit_other_experiences'))

    return render_template('add_other_experience.html')

# Route to edit an existing other experience
@admin_views.route('/admin/edit_other_experience/<int:exp_id>', methods=['GET', 'POST'])
@login_required
def edit_other_experience(exp_id):
    if request.method == 'POST':
        title = request.form['title']
        company = request.form['company']
        start_date = request.form['start_date']
        end_date = request.form.get('end_date')  # Optional
        location = request.form['location']
        description = request.form['description']

        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE other_experience
            SET title = %s, company = %s, start_date = %s, end_date = %s, location = %s, description = %s
            WHERE id = %s
        """, (title, company, start_date, end_date, location, description, exp_id))
        conn.commit()
        conn.close()

        flash('Other Experience updated successfully!', 'success')
        return redirect(url_for('admin.edit_other_experiences'))

    experience = get_other_experience_by_id(exp_id)
    if not experience:
        flash('Other Experience not found!', 'danger')
        return redirect(url_for('admin.edit_other_experiences'))

    return render_template('edit_other_experience_form.html', experience=experience)

# Route to delete an other experience
@admin_views.route('/admin/delete_other_experience/<int:exp_id>', methods=['POST'])
@login_required
def delete_other_experience(exp_id):
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM other_experience WHERE id = %s", (exp_id,))
    conn.commit()
    conn.close()

    flash('Other Experience deleted successfully!', 'success')
    return redirect(url_for('admin.edit_other_experiences'))

####################################### BLOG ##############################################
def generate_slug(title):
    """
    Generate a unique slug using the title and a UUID.
    """
    return f"{title.replace(' ', '-').lower()}-{uuid.uuid4().hex[:8]}"

def format_datetime(timestamp):
    """
    Converts a datetime object into a human-readable format and adjusts to Eastern Time (ET).
    """
    if not isinstance(timestamp, datetime):
        raise TypeError("timestamp must be a datetime object")

    # Assuming the input timestamp is in UTC, convert to ET
    utc = pytz.utc
    eastern = pytz.timezone("US/Eastern")
    dt = utc.localize(timestamp).astimezone(eastern)

    return dt.strftime("%B %d, %Y • %I:%M %p ET")



def get_all_blog_posts():
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, title, content, visibility, created_at, updated_at, slug
        FROM blog_posts
        ORDER BY created_at DESC
    """)
    posts = cursor.fetchall()
    conn.close()

    # Format the dates for each post
    formatted_posts = [
        (post[0], post[1], post[2], post[3],
         format_datetime(post[4]),  # Format created_at
         format_datetime(post[5]) if post[5] else None,
         post[6])  # Format updated_at (if exists),
        for post in posts
    ]
    return formatted_posts

def get_blog_post_by_id(post_id):
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, title, content, visibility, created_at, updated_at, slug
        FROM blog_posts
        WHERE id = %s
    """, (post_id,))
    post = cursor.fetchone()
    conn.close()

    if post:
        return (
            post[0], post[1], post[2], post[3],
            format_datetime(post[4]),  # Format created_at
            format_datetime(post[5]) if post[5] else None,  # Format updated_at (if exists),
            post[6]
        )
    return None

# Route to display all posts (for logged-in admin)
@admin_views.route('/admin/manage_blog', methods=['GET'])
@login_required
def manage_blog():
    posts = get_all_blog_posts()
    return render_template('manage_blog.html', posts=posts)

# Route to add a new blog post
@admin_views.route('/admin/add_blog_post', methods=['GET', 'POST'])
@login_required
def add_blog_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        visibility = request.form['visibility']

        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()
        slug = generate_slug(title)
        cursor.execute("""
            INSERT INTO blog_posts (title, content, visibility, slug)
            VALUES (%s, %s, %s, %s)
        """, (title, content, visibility, slug))
        conn.commit()
        conn.close()

        flash('Blog post added successfully!', 'success')
        return redirect(url_for('admin.manage_blog'))

    return render_template('add_blog_post.html')


@admin_views.route('/admin/edit_blog_post/<int:post_id>', methods=['GET', 'POST'])
@login_required
def edit_blog_post(post_id):
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        visibility = request.form['visibility']
        updated_at = datetime.utcnow()  # Store UTC time in the database

        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()
        
        # Update existing blog post
        cursor.execute("""
            UPDATE blog_posts
            SET title = %s, content = %s, visibility = %s, updated_at = %s
            WHERE id = %s
        """, (title, content, visibility, updated_at, post_id))
        conn.commit()
        conn.close()

        flash('Blog post updated successfully!', 'success')
        return redirect(url_for('admin.manage_blog'))

    # Fetch the blog post to prefill the edit form
    post = get_blog_post_by_id(post_id)
    if not post:
        flash('Blog post not found!', 'danger')
        return redirect(url_for('admin.manage_blog'))

    return render_template('edit_blog_post.html', post=post)

# Route to delete a blog post
@admin_views.route('/admin/delete_blog_post/<int:post_id>', methods=['POST'])
@login_required
def delete_blog_post(post_id):
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM blog_posts WHERE id = %s", (post_id,))
    conn.commit()
    conn.close()

    flash('Blog post deleted successfully!', 'success')
    return redirect(url_for('admin.manage_blog'))

@admin_views.route('/blog/<slug>', methods=['GET'])
def view_blog_post(slug):
    post = None
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, title, content, visibility, created_at, updated_at
        FROM blog_posts
        WHERE slug = %s
    """, (slug,))
    row = cursor.fetchone()
    conn.close()

    if row:
        post = {
            "id": row[0],
            "title": row[1],
            "content": row[2],
            "visibility": row[3],
            "created_at": format_datetime(row[4]),
            "updated_at": format_datetime(row[5]) if row[5] else None
        }

    # Check visibility
    if not post or (post["visibility"] == "private" and not session.get("authenticated")):
        flash("Blog post not found or you do not have permission to view it.", "danger")
        return redirect(url_for("blogandphilosophy.blogandphilosophy"))

    return render_template("view_blog_post.html", post=post)

