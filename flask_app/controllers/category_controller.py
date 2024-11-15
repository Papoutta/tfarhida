from flask_app import app
from flask import render_template, redirect, request, session, flash # type: ignore
from flask_app.models.category_model import Category

#dashboard route
@app.route('/admin')
def admin_dashboard():
    all_categories=Category.get_all()
    return render_template('admin_dashboard.html',all_categories=all_categories)

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
