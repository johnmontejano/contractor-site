from flask import Flask, render_template, request, redirect, url_for
from bson.objectid import ObjectId
from pymongo import MongoClient
import os
from datetime import datetime

items = [
    {'product_title':'ferrari turbo car', 'price':22.00, 'description':'fastest car'},
    {'product_title':'lambo turbo car', 'price':42.00, 'description':'fastest car'},
    {'product_title':'toyota turbo car', 'price':22.00, 'description':'fastest car'}
]
client = MongoClient()
db = client.Shop
products = db.products

# products.insert_many([
#     {'product_title':'ferrari turbo car', 'price':22.00, 'description':'fastest car'},
#     {'product_title':'lambo turbo car', 'price':42.00, 'description':'fastest car'},
#     {'product_title':'toyota turbo car', 'price':22.00, 'description':'fastest car'}
# ])
app = Flask(__name__)
@app.route('/')
def home_index():
    '''Create the item'''
    return render_template('index.html', items=items)
if __name__ == ("__main__"):
    app.run(debug=True)

