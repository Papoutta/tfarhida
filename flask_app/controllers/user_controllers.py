from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user_models import User 
from flask_bcrypt import Bcrypt  
bcrypt=Bcrypt(app)
@app.route("/") 
def index():
    return render_template("index.html") 
def register():
    pw=bcrypt.generate_password_hash(request.form["password"])  
    data={ 
            **request.form,
            "password":pw
    } 
    user_id=User.register(data) 
    session["user_id"]=user_id 
    return redirect("/home.html ") 























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
