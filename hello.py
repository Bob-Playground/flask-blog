from flask import Flask
from flask import request
from flask import redirect
from flask import abort
from flask import render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<string:name>')
def user(name):
    return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
    
# 重定向示例
@app.route('/mi')
def mi():
    return redirect('http://youpin.mi.com')

# abort 示例
@app.route('/invalid')
def invalid():
    abort(404)

# # 代码启动 flask
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

# 命令行启动 flask
# export FLASK_APP=hello.py
# export FLASK_DEBUG=1
# flask run --host 0.0.0.0