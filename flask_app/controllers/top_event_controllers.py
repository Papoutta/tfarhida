from flask_app import app
from flask import render_template, session
from flask_app.models.create_event_model import Event 
from flask_app.models.user_models import User 


###################### top events ############################################
@app.route("/top_events") 
def top_events():
    top_events= Event.get_top_events()
    return render_template("top_events.html", top_events=top_events) 

####################### categorise########################################### 

@app.route("/categories") 
def categories():
    all_events = Event.get_all_events()
    loggedin_user= User.get_user({"id":session['user_id'] })
    return render_template("categories.html", all_events = all_events, loggedin_user =loggedin_user )
