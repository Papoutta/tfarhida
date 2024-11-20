from flask_app import app
from flask import render_template,request,session,redirect
from flask_app.models.user_models import User   
from flask_app.models.likes_models import Like 
@app.route("/likes/add",methods=["POST"]) 

    
@app.route('/likes/add', methods=['post'])
def likes_add():
    data={
        **request.form,
        "user_id": session['user_id']
    }
    Like.likes(data)
    user= User.get_user({'id': session['user_id']})
    first_category= user.interests[0]
    return redirect(f'/home/{first_category}')
@app.route('/likes/delete', methods=['post'])
def likes_delte():
    data={
        **request.form,
        "user_id": session['user_id']
    }
    Like.delte(data)
    user= User.get_user({'id': session['user_id']})
    first_category= user.interests[0]
    return redirect(f'/home/{first_category}')


