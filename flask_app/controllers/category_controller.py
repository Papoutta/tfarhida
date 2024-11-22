from flask_app import app
from flask import render_template, redirect, request, session, flash # type: ignore
from flask_app.models.category_model import Category
from flask_app.models.user_models import User

#dashboard route
@app.route('/admin')
def admin_dashboard():
    all_categories=Category.get_all()
    all_users = User.get_all_users()
    loggedin_user= User.get_user({"id":session['user_id'] })
    return render_template('admin_dashboard.html',all_categories=all_categories, all_users = all_users, loggedin_user=loggedin_user)

#Action route to create category
@app.route('/admin/create_category', methods = ['POST'])
def create_category():
    if Category.validate(request.form) :
        data={
            **request.form
        }
        Category.create(data)
        return redirect('/admin')
    return redirect('/admin')

@app.route("/delete_user/<int:id>", methods = ['POST'])
def delete_user(id):
    User.delete_user({'id':id})
    return redirect("/admin")