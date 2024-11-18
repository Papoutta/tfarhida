from flask_app import app
from flask import render_template
from flask_app.models.category_model import Category


@app.route('/informations')
def informations():
    all_categories=Category.get_all()
    return render_template('informations.html',all_categories=all_categories)
    # to change by id category and not all categories