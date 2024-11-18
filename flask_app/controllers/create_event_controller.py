from flask_app import app
 
from flask import render_template,redirect,request,session,flash
from flask_app.models.category_model import Category 
from flask_app.models.create_event_model import Event

@app.route('/event')
def event():
    all_categories=Category.get_all()
    return render_template('create_events.html',all_categories=all_categories) 


@app.route("/create/event", methods=["POST"])
def create_event() : 
    data={ 
        **request.form,  
        } 
    Event.save(data)
    return redirect("/home") 


