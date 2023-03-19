from flask import Flask, request, Response, url_for, redirect, session
from flask import render_template, flash

app = Flask(__name__)

app.secret_key = '\xc0\xc1'


@app.route('/<name>')
def index(name):
    if 'username' in session :
        return render_template('complete_index.html', name=name)
    else:
        return render_template('complete_login.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username']!='admin' or\
                request.form['password']!='123456':
            flash('username or password invaild')
            return redirect(url_for('index', name="shiyan"))
        else:
            session['username'] = request.form['username']
            name = request.form['username']
            print(name)
            app.logger.debug(name)
            flash("you were logged in")
            return redirect(url_for('index', name=name))
    return render_template('complete_login.html')
