from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/user/<username>')
def user_index(username):
    return f'Hello {username}'


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'

@app.errorhandler(404)
def not_found(e):
    return '没找到', 404


if __name__ == '__main__':
    app.run()
