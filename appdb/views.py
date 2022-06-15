

from appdb import app
from flask import render_template




@app.route("/")
def home():
	
    return render_template('index.html')


@app.route('/product')
def product():

    return render_template('products/product.html')

@app.route('/contact')
def contact():
    return render_template('home/layout/contact.html')

@app.route('/introduce')
def introduce():
    return render_template('home/layout/introduce.html')