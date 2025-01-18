from flask import Blueprint, request, redirect, url_for, flash, render_template, session
import psycopg2
import bcrypt
import os

login_views = Blueprint('login', __name__)
DATABASE_URL = os.getenv("DATABASE_URL")

# Helper function to connect to the database
def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn

@login_views.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form.get('password')

        # Connect to the database and fetch the stored hashed password
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT password FROM password LIMIT 1')  # Fetch stored hashed password
        result = cursor.fetchone()
        conn.close()

        if result and bcrypt.checkpw(password.encode('utf-8'), result[0].encode('utf-8')):
            session['authenticated'] = True
            return redirect(url_for('admin.admin'))  # Assuming an admin panel route exists
        else:
            error_message = "Incorrect password. Please try again."
            return render_template('login.html', error=error_message)

    return render_template('login.html')

@login_views.route('/logout')
def logout():
    # Remove 'authenticated' from session to log the user out
    session.pop('authenticated', None)
    return redirect(url_for('login.login'))
