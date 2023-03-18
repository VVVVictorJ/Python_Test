from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!'

@app.route('/<name>')
def get_name(name):
    return name

@app.route('/sum/<int:a>/<int:b>')
def get_sum(a, b):
    return str(a+b)
