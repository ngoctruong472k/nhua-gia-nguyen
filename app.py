from flask import render_template
from appdb import app

@app.route("/")
def home():
    return render_template('home/index.html')

@app.route("/news")
def news():
    return render_template('home/news/news.html')

@app.route("/introduce")
def introduce():
    return render_template('home/news/introduce.html')

@app.route("/contact")
def contact():
    return render_template('home/news/contact.html')



if __name__ == "__main__":
    app.run(debug=True)