from appdb import app
from flask import render_template
from flask_pymongo import PyMongo


# app.config['MONGO_URI'] = "mongodb://localhost:27017/nhuagianguyen"
# mongo = PyMongo(app)
cluster = "mongodb+srv://test:<root123>@cluster0.bmlyl.mongodb.net/?retryWrites=true&w=majority"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/sanpham")
def products():
    return render_template("products/product.html")


@app.route("/contact")
def contact():
    return render_template("home/layout/contact.html")


@app.route("/introduce")
def introduce():
    return render_template("home/layout/introduce.html")


@app.route("/admin")
def admin():
    return render_template("admin/admin.html")
