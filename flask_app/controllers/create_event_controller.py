from flask_app import app
from flask import rendem_template

@app.route('/create_event')
def create_event():
    return render_template('create_event.html')