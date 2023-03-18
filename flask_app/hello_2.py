 1 from flask import request
 
@app.route('/login', methods=['POST'], ['GET'])
def login():
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # 当请求形式为"GET"或者认证失败则执行以下代码
    return render_template('login.html', error=error)
