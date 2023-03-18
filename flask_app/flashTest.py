from flask import Flask, flash, redirect, render_template, \
        request, url_for


app = Flask(__name__)
app.secret_key = '\xc0\xc1\x90\xb1\xf7\xb2-Ns\xf1\xe4\x04vw\x88\x18'

@app.route('/')
def index():
    return render_template('index_1.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username']!='admin' or \
                request.form['password']!='secret':
            print(request.form['username']+request.form['password'])
            error = 'Invaild credentials'
        else:
            flash('You were sucessfully logged in')
            # url_for跳转至index函数
            return redirect(url_for('index'))
    return render_template('login.html', error=error)
