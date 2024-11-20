from flask_app import app
from flask import render_template,request,session,redirect
from flask_app.models.category_model import Category   
from flask_app.models.likes_models import Like 
@app.route("/likes/add",methods=["POST"]) 

    
@app.route('/likes/add', methods=['post'])
def likes_add():
    data={
        **request.form,
        "user_id": session['user_id']
    }
    Like.likes(data)
    return redirect('/home')
@app.route('/likes/delete', methods=['post'])
def likes_delte():
    data={
        **request.form,
        "user_id": session['user_id']
    }
    Like.delte(data)
    return redirect('/home')


