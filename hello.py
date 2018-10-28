from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/user/<string:name>')
def user(name):
    return '<h1>Hello {}!</h1>'.format(name)

# 代码启动 flask
# if __name__ == '__main__':
#     app.run(debug=True)

# 命令行启动 flask
# export FLASK_APP=hello.py
# export FLASK_DEBUG=1
# flask run --host 0.0.0.0