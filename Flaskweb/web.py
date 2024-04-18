from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')  # 1. 创建了网站和函数index的对应关系
def index():
    return render_template("index.html") #默认读取 templates 文件中的html 格式数据
def get_news():
    return render_template("get_news.html")

"""
html格式的标签分类：
    1.行内标签
        <div></div>
        <h1>hello world</h1>
    2.块级标签
    
    


"""


if __name__ == '__main__':
    app.run(debug=True)

