from flask import Flask
from flask import request
from flask import redirect
from flask import abort

app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('user_agent')
    print(request)
    return '<p>Your browser is {}</p>'.format(user_agent)

@app.route('/user/<string:name>')
def user(name):
    return '<h1>Hello {}!</h1>'.format(name)

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
    app.run(debug=True)

# 命令行启动 flask
# export FLASK_APP=hello.py
# export FLASK_DEBUG=1
# flask run --host 0.0.0.0