from flask_app import app
from flask import render_template # type: ignore

@app.route('/home_after_login')
def home_after_login():
    return render_template('home_after_login.html')