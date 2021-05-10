"""Script to seed database."""

import os
import json
from random import choice, randint

import crud
import model
import server

os.system('dropdb products')
os.system('createdb products')

model.connect_to_db(server.app)
model.db.create_all()

# Load product data from JSON file
with open('data/products.json') as f:
    product_data = json.loads(f.read())

# Create products, store them in list
products_in_db = []
for product in product_data:
    brand, name, category, tag, img_path = (product['brand'], 
                                            product['name'], 
                                            product['category'], 
                                            product['tag'], 
                                            product['img_path'])

    db_product = crud.create_product(brand, name, category, tag, img_path)
   
    products_in_db.append(db_product)
