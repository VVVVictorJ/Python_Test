import json

import flask
from flask import (Flask, abort, flash, g, jsonify, redirect, render_template,
                   request, session, url_for)

ENV = 'development'
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/getData', methods=['POST'])
def testGetData():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json;charset=UTF-8'):
        jsonj = request.json
        # print(jsonj)
        # print(type(jsonj))
    else:
        print("error")
    return jsonify({'data':jsonj['id']})
    # return request.headers.get('Content-Type')

if __name__ == '__main__':
    app.run()