import requests
from flask import Flask, request


app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'


@app.route('/user/<username>')
def user_index(username):
    print('User-Agent:', request.headers.get('User-Agent'))
    print('time:', request.args.get('time'))
    print('q:', request.args.get('q'))
    print('Q:', request.args.getlist('Q'))
    return f'Hello {username}'

@app.route('/register', methods=['GET', 'POST'])   # 如果需要处理 POST 请求，就需要指定 methods=['GET', 'POST']
def register():
    print('method:', request.method)                     # 查看本次请求的方式
    print('name:', request.form.get('name'))             # 获取 name 值
    print('password:', request.form.get('password'))     # 获取 password 值
    print('hobbies:', request.form.getlist('hobbies'))   # 获取 hobbies 值，因为有多项使用 getlist 方法
    print('age:', request.form.get('age', default=18))   # 如果没有传递 age 值，可以在程序中设置默认值
    return 'registered successfully!'

@app.route('/httptest', methods=['POST', 'GET'])
def httptest():
    if request.method == 'POST':
        print('Q:', request.form.get('Q'))
        print('It is a post request!')
    elif request.method == 'GET':
        print('t:', request.args.get('t'), 'q:', request.args.get('q'))
        print('It is a get request!')
    return ''
