from flask import Flask
from flask import abort, redirect, url_for
from flask import render_template


app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()

# 定制错误页面
@app.errorhandler(401)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

# 响应
# 一个视图函数的返回值会被自动转换为一个响应对象。
# 如果返回值是一个字符串，它会被转换成一个响应主体是该字符串，
# 错误代码为200 OK，媒体类型为text/html的响应对象。
# Flask 把返回值转换成响应对象的逻辑如下：
# 1. 如果返回的是一个合法的响应对象，它会直接从视图返回
# 2. 如果返回的是一个字符串，响应对象会用字符串数据和默认参数创建
# 3. 如果返回的是一个元组而且元组中元素能够提供额外的信息。这样的元组必须是
# （response，status， headers）且至少含有其中的一个元素。
# status值将会覆盖状态代码，headers可以是一个列表或额外的消息头 值字典
# 4.如果上述条件均不满足，Flask会假设返回值是一个合法的WSGI应用程序，
# 并转换为一个请求对象

# 假设有下面一个视图
#@app.errorhandler(404)
#def not_found(error):
#    return render_template('error.html'), 404

@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('error.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp

