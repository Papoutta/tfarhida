from flask_app import app
from flask import render_template


@app.route('/user')
def user_by_id():
    return render_template('profile.html')

