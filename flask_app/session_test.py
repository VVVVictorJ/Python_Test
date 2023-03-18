from flask import Flask, session, redirect, url_for, escape, request


app = Flask(__name__)


# 设置密钥，保证会话安全
app.secret_key='\xc0\xc1\x90\xb1\xf7\xb2-Ns\xf1\xe4\x04vw\x88\x18'

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as {}'.format(escape(session['username']))
    return 'You are not logged in'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
    <form method="POST">
        <p><input type=text name=username>
        <p><input type=submit value=Login>
    </form>
    '''

@app.route('/logout')
def logout():
    # 如果用户名存在，则从会话中移除该用户名
    session.pop('username', None)
    return redirect(url_for('index'))

