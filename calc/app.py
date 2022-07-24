# Put your app in here.
from flask import Flask, request
import operations 
app = Flask(__name__)

@app.route('/add')
def do_add():
    a = int(request.args.get("a"))
    b = int(request.args.get('b'))
    result = operations.add(a,b)
    return str(result)

@app.route('/sub')
def do_sub():
    a = int(request.args.get("a"))
    b = int(request.args.get('b'))
    result = operations.sub(a,b)
    return str(result)

@app.route('/mult')
def do_mult():
    a = int(request.args.get("a"))
    b = int(request.args.get('b'))
    result = operations.mult(a,b)
    return str(result)

@app.route('/div')
def do_div():
    a = int(request.args.get("a"))
    b = int(request.args.get('b'))
    result = operations.div(a,b)
    return str(result)