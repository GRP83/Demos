# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, render_template
#from flask_bootstrap import Bootstrap
app = Flask(__name__)
#Bootstrap(app)

@app.route("/")
def hello():
    return render_template('login.html')

@app.route("/index")
def index():
    return render_template('home.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/logout")
def logout():
    return render_template('logout.html')

@app.route("/home")
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run()
    #Bootstrap(app)
