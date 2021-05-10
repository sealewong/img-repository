"""Model for hair product image repository."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Product(db.Model):
    """A hair product."""

    __tablename__ = 'products'

    product_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    brand = db.Column(db.String)
    name = db.Column(db.String)
    category = db.Column(db.String)
    tag = db.Column(db.String)
    img_path = db.Column(db.String, unique=True)

    def __repr__(self):
        return f'<Product product_id={self.product_id} brand={self.brand} name={self.name}>'


def connect_to_db(flask_app, db_uri='postgresql:///products', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app