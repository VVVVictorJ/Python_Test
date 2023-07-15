import json

import flask
from flask import (
    Flask,
    abort,
    flash,
    g,
    jsonify,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

ENV = "development"
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/getData", methods=["POST"])
def testGetData():
    content_type = request.headers.get("Content-Type")
    if content_type == "application/json;charset=UTF-8":
        jsonj = request.json
        # print(jsonj)
        # print(type(jsonj))
    else:
        print("error")
    return jsonify({"data": jsonj["id"]})
    # return request.headers.get('Content-Type')


@app.route("/ReceiveFile", methods=["POST"])
def getDocx():
    data = request.files
    file = data["file"]
    print(file.filename)
    print(request.headers)
    file.save(file.filename)
    return "已接受保存\n"


@app.route("/test", methods=["POST"])
def test():
    name = request.form.get("name")
    sex = request.form.get("sex")
    print("name:", name, "sex:", sex)
    return "Hello World!"

@app.route("/testJson", methods=["POST"])
def testJson():
    print(request.json['name'])
    print(request.json['sex'])
    return request.json


if __name__ == "__main__":
    app.run()
