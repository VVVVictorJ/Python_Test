from flask import Flask


app = Flask(__name__)
app.config.update({
    'SECRET_KEY':'a random string',
    })


@app.route('/')
def index():
    return '另一种启动方式的 =>Hello World!'

@app.route('/a')
def index_a():
    return 'hellp'

@app.route('/user/<username>')
def user_index(username):
    return f'Hello {username}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'

@app.route('/courses/<name>')
def courses(name):
    return f'Courses:{name}'

if __name__ == '__main__':
    for k, v in app.view_functions.items():
        print(f'{k} -- {v}')
    app.run()
