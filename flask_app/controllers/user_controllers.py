from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user_models import User   
from flask_app.models.category_model import Category 
from flask_app.models.intersts_models import Interests
from flask_app.models.create_event_model import Event
from flask_bcrypt import Bcrypt  
bcrypt=Bcrypt(app)
@app.route('/')
def home():
    return render_template('home.html')

@app.route("/users") 
def index():
    return render_template('index.html')
@app.route("/users/create",methods=["POST"]) 

def register(): 
    if User.validate(request.form):
        pw=bcrypt.generate_password_hash(request.form["password"])
        data={ 
            **request.form,  
            "password":pw
        } 
        print(data,"**********************************")
        user_id=User.register(data)
        session["user_id"]=user_id
        return redirect("/choos")
    else:  
        return redirect("/users") 


@app.route("/choos")
def choos(): 
    all_categories=Category.get_all()
    return render_template("interset.html",all_categories=all_categories)


@app.route("/choose",methods=["POST"])
def choose(): 

    checked_options = request.form.getlist('choose')
    print("**********************")
    print(checked_options)
    #  session["categories"]=checked_options
    for c in checked_options: 
        print("==============================")
        print(c)
        Interests.creat({"user_id":session['user_id'] ,"category_id":int(c)}) 
    return redirect(f"/home/{int(checked_options[0])}" )


@app.route('/home/<int:category_id>')
def home_after_login(category_id):
    my_interest_events = Event.get_user_events({"categories_id":category_id})
    # user_events = Event.get_events_with_joined_users()
    loggedin_user= User.get_user({"id":session['user_id'] })
    # all_groups = Event.get_all_groups({"users_id":session['user_id'] })
    print("***************")
    print(loggedin_user.interests)
    # print(loggedin_user.id)
    return render_template('home_after_login.html',my_interest_events = my_interest_events, loggedin_user=loggedin_user)


@app.route("/welcome",methods=["POST"])
def login():
    user=User.get_by_email({'email':request.form["email"]})
    if not user: 
        flash("invalid email/pasword")
        return redirect('/users') 
    if not bcrypt.check_password_hash(user.password,request.form['password']):
        flash("invalid email/pasword")
        return redirect('/users') 
    session["user_id"]=user.id 
    print("*****************", user.interests[0])
    id= user.interests[0]['category_id']
    return redirect(f"/home/{id}") 


@app.route("/contact_us") 
def contact_us():
    return render_template("contact.html")


# @app.route("/logout") 
# def logout():
#     session.clear()
#     return redirect("/")  
