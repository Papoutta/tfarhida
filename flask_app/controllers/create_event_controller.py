from flask_app import app
 
from flask import Flask, flash, request, redirect, url_for, render_template
import urllib.request
import os
from werkzeug.utils import secure_filename
from flask_app.models.category_model import Category 
from flask_app.models.create_event_model import Event

UPLOAD_FOLDER = os.path.join('flask_app', 'static', 'img')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/event')
def event():
    all_categories=Category.get_all()
    return render_template('create_events.html',all_categories=all_categories)  


# Route to create an event
@app.route("/create/event", methods=["POST"])
def create_event():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    
    if file and allowed_file(file.filename):
        # Secure the filename and save the file
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Prepare data for saving to the database
        data = {
            **request.form,
            'image_path': filepath  # Include the file path for database storage
        }

        # Save the event (assuming `Event.save` is a custom method)
        Event.save(data)
        
        # Flash success and render a template to display the uploaded image
        flash('Image successfully uploaded and event created!')
        return render_template('create_events.html', img=filename)
    else:
        flash('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)


    

