from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/addparcel')
def addparcel():
    return render_template('add_parcel.html')
