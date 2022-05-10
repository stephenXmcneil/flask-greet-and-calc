# Put your app
from flask import Flask, request

app = Flask(__name__)

@app.route('/addition')
def addition():
    a = request.arg["a"]
    b = request.arg["b"]
    return a + b
    
@app.route('/addition')
def addition():
    a = request.arg["a"]
    b = request.arg["b"]
    return b - a

@app.route('/addition')
def addition():
    a = request.arg["a"]
    b = request.arg["b"]
    return a * b

    
@app.route('/addition')
def addition():
    a = request.arg["a"]
    b = request.arg["b"]
    return a / b