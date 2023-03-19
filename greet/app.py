from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome_msg():
    return "welcome"

@app.route('/welcome/<type>')
def welcome_type(type):
    return f"welcome {type}"