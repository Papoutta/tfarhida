from flask_app import app
from flask import render_template, redirect, request, session, flash # type: ignore
from flask_app.models.category_model import Category


@app.route('/admin')
def index_admin():
    return redirect('/admin')

#dashboard route
@app.route('/admin')
def admin_dashboard():
    all_categories=Category.get_all()
    return render_template('admin_dashboard.html',all_categories=all_categories)

#Action route to create category
@app.route('/admin/create_category', methods = ['POST'])
def create_category():
    data={
        **request.form
    }
    Category.create(data)
    return redirect('/admin')