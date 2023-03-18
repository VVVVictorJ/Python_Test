from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def get_hello():
    return render_template('hello_1.html')
