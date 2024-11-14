from flask_app import app
from flask import render_template # type: ignore

@app.route('/')
def home():
    return render_template('home.html')