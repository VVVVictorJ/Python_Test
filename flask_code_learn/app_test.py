from flask import Flask
from flask import redirect, url_for


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'

@app.route('/user/<username>')
def Hello(username):
    if username == 'victor':
        return f'Hello {username}'
    #return redirect(url_for('index'))
    return redirect('/', 303)

@app.route('/user/<username>')
def user_index(username):
    return f'Hello {username}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'

@app.route('/test')
def test():
    print(url_for('index'))
    print(url_for('user_index', username='shiyan'))
    print(url_for('show_post', post_id=2, _external=True))
    print(url_for('show_post', post_id=2, q='python 03'))
    print(url_for('show_post', post_id=2, q='python你好'))
    print(url_for('show_post', post_id=2, _anchor='a'))
    return 'test'

@app.route('/test')
def test():
    print('xxx.simplelab.cn/courses/java')
    return redirect('/', 301)
