from flask import Flask, render_template


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
def index():

    teacher = {
            'name': 'Aiden',
            'email': 'luojin@simplecloud.cn'
    }

    course = {
            'name':'Python Basic',
            'teacher': teacher,
            'user_count': 5348,
            'price': 199.0,
            'lab':None,
            'is_private':False,
            'is_member_course': True,
            'tags':['python', 'big data', 'Linux']
    }
    return render_template('index.html', course=course)

@app.route('/course')
def course():
    course = {
            'python': 'lou+ python',
            'java': 'java base',
            'bigdata': 'spark sql',
            'teacher': 'shixiaolou',
            'is_unique': False,
            'has_tag': True,
            'tags': ['c', 'c++', 'docker']
    }
    return render_template('index_new.html', course=course)
