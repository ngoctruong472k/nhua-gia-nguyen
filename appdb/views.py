from appdb import app
from flask import render_template,url_for



@app.route('/')
def index():
	return render_template('home/layout/layout.html')

@app.route('/main')
def main():
	return render_template('home/layout/main.html')

@app.route('/product')
def product():
	return render_template('products/product.html')
 