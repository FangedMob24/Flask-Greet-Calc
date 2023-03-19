# Put your app in here.
from flask import Flask, request
from operations import add,mult,sub,div

app = Flask(__name__)

@app.route("/add")
def adding():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    value = add(a,b)
    return str(value)

@app.route("/sub")
def subtration():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    value = sub(a,b)
    return str(value)

@app.route("/mult")
def multiply():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    value = mult(a,b)
    return str(value)

@app.route("/div")
def divide():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    value = div(a,b)
    return str(value)

@app.route("/math/<operation>")
def calc(operation):
    operations = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div
    }
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    value = operations[operation](a,b)
    return str(value)