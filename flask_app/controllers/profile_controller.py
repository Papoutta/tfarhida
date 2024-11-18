from flask_app import app
from flask import render_template # type: ignore  
from flask import render_template,redirect,request,session,flash
from flask_app.models.user_models import User 

@app.route('/profile')
def profile():
    return render_template('profile.html')  
@app.route('/edite_your_information/<int:id>')
def edite_your_information(id): 
    user=User.get_user({"id":id})

    return render_template('edit_your_information.html',user=user )

@app.route("/profile/<int:id>/update",methods=["POST"]) 
def update(id): 
    if User.validate(request.form):

        data={ 
         **request.form, 
            "id":id
        } 
        User.update(data) 
        return redirect("/profile") 
    return redirect(f"/profile/{id}/update") 