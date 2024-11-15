from flask_app import app
from flask import render_template # type: ignore

@app.route('/profile')
def profile():
    return render_template('profile.html')