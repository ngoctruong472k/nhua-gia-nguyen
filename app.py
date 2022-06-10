from flask import render_template
from appdb import app

@app.route("/")
def home():
    return render_template('home/index.html')

@app.route("/news")
def news():
    return render_template('home/news/index.html')

if __name__ == "__main__":
    app.run(debug=True)