import sqlite3
from flask import (Flask, render_template, g, flash, request, session, abort,
                   redirect, url_for)


# 配置项
DATABASE = '/tmp/flaskr.db'
ENV = 'development'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'


# 创建应用
app = Flask(__name__)
# app.config 的from_object 方法通常用于获取对象的属性以增加配置
# 此处使用的参数为__name__, 也就是当前所在文件
# 结果就是读取当前所在文件中的所有变量，选择其中全大写的变量作为配置项
app.config.from_object(__name__)
# 也可以将配置存储到多个文件
# app.config.from_envvar('FLASKR_SETTINGS', silent=True)
# 静默开关silent=True告诉 Flask 不去关心这个环境变量键值是否存在。

def db_conn():
    '''
    创建与数据库连接的对象
    '''
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    '''
    此函数用于创建数据表， 需要在flask shell 里引入执行
    '''

    # db_conn 函数的返回值是sqlite3.connect 方法的返回值
    # sqlite3.connect 方法的返回值是具有 __enter__ 和__exit__两个特殊方法的
    # 上下文对象
    # 这个上下文对象也叫连接对象，它的存在就是和sqlite3 数据库保持连接的标志
    # 其中as 关键字后面的conn 就是连接对象，该对象有一个close方法用于关闭连接
    # 此处使用with关键字处理 sqlite3.connect 方法的返回值
    # 使得with语句块内的代码运行完毕后自动执行连接对象conn的close方法关闭连接
    with db_conn() as conn:
        # 连接对象conn 的cursor方法的返回值是一个光标对象，用于执行SQL语句
        # 该光标对象通常使用execute 执行SQL语句，参数为语句的字符串
        # 光标对象的executescript 可以一次执行多个SQL语句
        # 参数为多个语句的二进制格式，多个语句通常写到一个文件里
        with app.open_resource('schema.sql') as f:
            conn.cursor().executescript(f.read().decode())
        # 连接对象的commit方法用于提交之前执行SQL语句的结果到数据库
        # 因为有些语句执行后不会立即改动数据库
        conn.commit()

# 这个装饰器的功能是，当任意视图函数执行时，预先执行这个装饰器下的所有函数
@app.before_request
def before():
    '''创建数据库的连接对象，并将其赋值给g的conn属性'''

    # Flask应用中有两种上下文对象：应用上下文对象和请求上下文对象
    # g 是一个应用上下文对象，它的生存周期却是一次请求的收发
    # 也就是说，应哟个每收到一次请求就会生成一个g对象
    # 在生存周期内，它可以在任意视图函数中被使用
    g.conn = db_conn()

# 与app.before_request 相对的是 app.after_request
# 后面在任意视图函数执行完毕之后执行，除非视图函数执行时遇到异常
# 而app.teardown_request 装饰器与app.after_request 作用一样
# 但它无视视图函数触发的任何异常，保证一定被执行
# 其中的参数为可能出现的异常
@app.teardown_request
def teardown(exception):
    '''关闭与数据库的连接'''
    

    g.conn.close()


@app.route('/')
def show_entries():
    '''显示所有存储在数据表中的条目'''

    # 获取连接对象执行查询操作之后的光标对象，该对象的fetchall方法中存储了查询结果
    cursor = g.conn.execute('SELECT title, text FROM entries ORDER BY id DESC')
    # 查询结果一个列表，列表里是元组，将元组转换成字典
    entries = [dict(title=row[0], text=row[1]) for row in cursor.fetchall()]
    return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    '''添加一条博客'''


    if not session.get('login'):
        abort(401)
    g.conn.execute('INSERT INTO entries (title, text) VALUES (?, ?)',
            [request.form.get('title'), request.form.get('text')])
    g.conn.commit()
    flash('New entry has beensuccessfully posted')
    return redirect(url_for('show_entries'))

@app.route('/login', methods=['GET', 'POST'])
def login():

    error =None
    if request.method == 'POST':
        if request.form.get('username')!=app.config.get('USERNAME'):
            error='Invalid username'
        # 如果密码与配置项不符
        elif request.form.get('password')!=app.config.get('PASSWORD'):
            error='Invalid password'
        else:
            session['login']=True
            flash('You\'re loginned successfully!')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    '''用户登出'''


    session.pop('login', None)
    flash('You have logouted successfully')
    return redirect(url_for('show_entries'))







if __name__ == '__main__':
    app.run()


























