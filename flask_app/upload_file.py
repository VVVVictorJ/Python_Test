import os
from flask import Flask, request
from werkzeug.utils import secure_filename

UPLOAD_FOLDER='/home/victor/flask_app'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            # secure_filename 会过滤中文
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return '{} 上传成功!'.format(filename)
    # 使用 GET 方式请求页面时或是上传文件失败时返回上传文件的表单页面
    return '''
    <!doctype html>
    <title>上传文件</title>
    <h1>上传文件</h1>
    <form action="" method=post enctype=multipart/form-data>
        <p><input type=file name=file>
            <input type=submit value=上传></p>
        </form>
    '''
