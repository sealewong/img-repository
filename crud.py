"""CRUD operations."""

from model import db, Product, connect_to_db


def create_product(brand, name, category, tag, img_path):
    """Create and return a new product."""

    product = Product(brand=brand, 
                      name=name, 
                      category=category, 
                      tag=tag, 
                      img_path=img_path)

    db.session.add(product)
    db.session.commit()

    return product


def get_products():
    """Return all products."""

    return Product.query.all()


def get_product(product_id):
    """Return a product by id."""

    return Product.query.get(product_id)


def get_products_by_brand(brand):
    """Return products by a certain brand."""

    return Product.query.filter(Product.brand==brand).all()


def get_products_by_category(category):
    """Return products in a certain category."""

    return Product.query.filter(Product.category==category).all()


def get_products_by_tag(tag):
    """Return products with a certain tag."""

    return Product.query.filter(Product.tag==tag).all()


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
