from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user_models import User   
from flask_app.models.category_model import Category 
from flask_app.models.intersts_models import Interests
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
        user_id=User.register(data)
        session["user_id"]=user_id
        return redirect("/choos")
    else:  
        return redirect("/users") 
######################################### INTERSERT ###################################################################################### 


@app.route("/choos")
def choos(): 
    all_categories=Category.get_all()
    return render_template("interset.html",all_categories=all_categories)
##############################
@app.route("/choose",methods=["POST"])
def choose(): 
 checked_options = request.form.getlist('choose')
 session["categories"]=checked_options
 for c in session["categories"]: 
    choos=Interests.creat({"user_id":session['user_id'] ,"category_id":c}) 
    return redirect("/home" )
####################################HOME########################################################################################### 
@app.route('/home')
def home_after_login():
    return render_template('home_after_login.html')
################################################## login##################################################################################### 
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
    return redirect('/home') 
################################################# update##############################################################################################

# @app.route('//<int:id>/edit' )
# def edit(id):  
#     party= .get_by_id({"id":id})
#     return render_template("edit.html", party=party)

# @app.route("/parties/<int:id>/update",methods=["POST"]) 
# def update(id): 
#     if Party.validate(request.form):
#         data={ 
#          **request.form, 
#             "id":id
#         } 
#         Party.update(data) 
#         return redirect("/dashboard") 
#     return redirect(f"/parties/{id}/edit") 


#############################contact######################################
@app.route("/contact_us") 
def contact_us():
    return render_template("contact.html")




























##########################################LOGIN#######################################################################################  

# @app.route("/login",methods=["POST"])
# def login():
#     user=User.get_by_email({'email':request.form["email"]})
#     if not user: 
#         flash("invalid email/pasword","login")
#         return redirect('/login') 
#     if not bcrypt.check_password_hash(user.password,request.form['password']):
#         flash("invalid email/pasword","login")
#         return redirect('/login') 
#     session["user_id"]=user.id 
#     return redirect('/home') 
# @app.route("/logout",methods=["POST"]) 
# def logout():
#     session.clear()
#     return redirect("/") 

###########################################edit##############################################################################################





















# def index():
#     return render_template("index.html")
# @app.route("/users/create",methods=["POST"]) 
# def register():
#     if User.validate(request.form):
#         pw=bcrypt.generate_password_hash(request.form["password"])
#         data={ 
#             **request.form,
#             "password":pw
#         } 
#         user_id=User.register(data) 
#         session["user_id"]=user_id
#         return redirect("/dashboard")
    
#     return redirect("/") 
# @app.route("/login",methods=["POST"])
# def login():
#     user=User.get_by_email({'email':request.form["email"]})
#     if not user: 
#         flash("invalid email/pasword","login")
#         return redirect('/') 
#     if not bcrypt.check_password_hash(user.password,request.form['password']):
#         flash("invalid email/pasword","login")
#         return redirect('/') 
#     session["user_id"]=user.id 
#     return redirect('/dashboard') 

# @app.route("/dashboard")
# def dashboard():   
#     if not 'user_id'in session:
#         return redirect('/')
#     logged_user=User.get_by_id({"id":session['user_id']})
#     return render_template("dashboard.html", logged_user=logged_user) 

# @app.route("/logout") 
# def logout():
#     session.clear()
#     return redirect("/")  
