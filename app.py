from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)
@app.route('/')
def home_index():
    '''Create the item'''
    return render_template('index.html')
    


