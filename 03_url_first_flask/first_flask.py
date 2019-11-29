# 从flask这个包中导入Flask
# Flask是这个项目的核心
from flask import Flask
# 创建一个Flask对象，传递__name__属性
app = Flask(__name__)


# @app.route('/')装饰器，
@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
