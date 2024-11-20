from flask_app import app
from flask import Flask, flash, request, redirect, url_for, render_template, session
import urllib.request
import os
from werkzeug.utils import secure_filename
from flask_app.models.category_model import Category 
from flask_app.models.create_event_model import Event
from flask_app.models.user_models import User
import uuid 

UPLOAD_FOLDER = os.path.join('flask_app', 'static', 'img')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/event')
def event():
    loggedin_user= User.get_user({"id":session['user_id'] })
    return render_template('create_events.html',loggedin_user=loggedin_user)  


# Route to create an event
@app.route("/create/event", methods=["POST"])
def create_event():
    if 'photo' not in request.files:
        flash('No file part')
        return redirect(request.url)
    
    file = request.files['photo']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    
    if file and allowed_file(file.filename):
        # Secure the filename and save the file
        filename = secure_filename(file.filename)
        unique_name = str(uuid.uuid4())+filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_name)
        file.save(filepath)
        
        # Prepare data for saving to the database
        data = {
            **request.form,
            'users_id' : session["user_id"],
            'photo': unique_name  # Include the file path for database storage
        }   

    #     # Save the event (assuming `Event.save` is a custom method)
        Event.save(data)   
        loggedin_user= User.get_user({"id":session['user_id'] })

        return redirect(f'/home/{loggedin_user.interests[0]["category_id"]}')
        
    #     # Flash success and render a template to display the uploaded image
    #     flash('Image successfully uploaded and event created!')
    #     return render_template('create_events.html', img=filename)
    # else:
    #     flash('Allowed image types are - png, jpg, jpeg, gif')
    #     return redirect(request.url)


@app.route('/groups/add', methods=['post'])
def add_to_group():
    data={
        **request.form,
        "users_id": session['user_id']
    }
    Event.add_to_group(data)
    loggedin_user= User.get_user({"id":session['user_id'] })

    return redirect(f'/home/{loggedin_user.interests[0]}')

@app.route('/groups/delete', methods=['post'])
def delete_from_group():
    data={
        **request.form,
        "users_id": session['user_id']
    }
    Event.delete_from_group(data)
    loggedin_user= User.get_user({"id":session['user_id'] })

    return redirect(f'/home/{loggedin_user.interests[0]}')