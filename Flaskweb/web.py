from flask import Flask

app = Flask(__name__)


@app.route('/')  # 1. 创建了网站和函数index的对应关系
def index():
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True)
