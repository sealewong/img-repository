"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def all_products():
    """View all products on homepage."""

    products = crud.get_products()

    return render_template('homepage.html', products=products)


@app.route('/brand/<brand>')
def brand_products(brand):
    """View products from a brand."""

    products = crud.get_products_by_brand(brand)

    return render_template('brand.html', products=products)


@app.route('/category/<category>')
def category_products(category):
    """View products of a category."""

    products = crud.get_products_by_category(category)

    return render_template('category.html', products=products)


@app.route('/tag/<tag>')
def tag_products(tag):
    """View products with a tag."""

    products = crud.get_products_by_tag(tag)

    return render_template('tag.html', products=products)


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
