from appdb import app
from flask import render_template


@app.route("/")
def home():
    return render_template('home/layout/layout.html')


@app.route('/product')
def product():
	return render_template('products/product.html')
 