from flask_app import app
from flask import render_template # type: ignore  
from flask import render_template,redirect,request,session,flash
from flask_app.models.user_models import User  
from flask_app.models.category_model import Category
from flask_app.models.create_event_model import Event


@app.route('/profile')
def profile():
    loggedin_user= User.get_user({"id":session['user_id'] })
    my_events= Event.get_my_events({"users_id":session['user_id'] })
    return render_template('profile.html', loggedin_user= loggedin_user, my_events = my_events)  

@app.route('/edite_your_information/<int:id>')
def edite_your_information(id): 
    user=User.get_user({"id":id})  
    all_categories=Category.intersts({"user_id":id}) 
    print(all_categories)
   
    return render_template('edit_your_information.html',user=user,all_categories=all_categories )

@app.route("/edite_your_information/<int:id>/update",methods=["POST"]) 
def update(id): 
    if User.validate(request.form):

        data={ 
         **request.form, 
            "id":id
        } 
        User.update(data) 
        return redirect("/profile") 
    return redirect("/profile/<int:id>") 


@app.route("/groups/deny_status", methods=['post'])
def deny_status():
    Event.deny_status(request.form)
    return redirect('/profile')



@app.route("/groups/accept_status", methods=['post'])
def accept_status():
    Event.accept_status(request.form)
    return redirect('/profile')