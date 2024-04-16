from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')  # 1. 创建了网站和函数index的对应关系
def index():
    return render_template("index.html") #默认读取 templates 文件中的html 格式数据


if __name__ == '__main__':
    app.run(debug=True)
