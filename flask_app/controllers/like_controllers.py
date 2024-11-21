from flask_app import app
from flask import render_template,request,session,redirect
from flask_app.models.user_models import User   
from flask_app.models.likes_models import Like  
from flask_app.models.reviews_models import Reviews 


    
@app.route('/likes/add', methods=['post'])
def likes_add():
    data={
        **request.form,
        "user_id": session['user_id']
    }
    Like.likes(data)
    user= User.get_user({'id': session['user_id']})
    first_category=user.interests[0]['category_id']
    return redirect(f'/home/{first_category}') 


@app.route('/likes/delete', methods=['post'])
def likes_delte():
    data={
        **request.form,
        "user_id": session['user_id']
    }
    Like.delte(data)
    user= User.get_user({'id': session['user_id']})
    first_category=user.interests[0]['category_id']
    return redirect(f'/home/{first_category}') 




@app.route('/comment', methods=['post'])
def comment():
    data={
        **request.form,
        "users_id": session['user_id']
    }
    Reviews.reviews(data)
    event_id=request.form['events_id']
    return redirect(f'/events/{event_id}')   
