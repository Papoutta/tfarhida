from flask_app import app
from flask import render_template
from flask_app.models.category_model import Category 


###################### top events ############################################
@app.route("/top_events") 
def top_events():
    return render_template("/top_events.html") 

####################### categorise########################################### 

@app.route("/categories") 
def categories():
    return render_template("catgorise.html")
