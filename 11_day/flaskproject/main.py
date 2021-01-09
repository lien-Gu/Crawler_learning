from flask import Flask,render_template

# 创建Flask对象实例
app=Flask(__name__)

#路由
@app.route('/')
def index():
    # return 'hello world!'
    return render_template('index.html')
@app.route('/login')
def login():
    return 'login...'

@app.route('/nei_page1')
def nei_page1():
    return render_template('nei_page1.html')

if __name__=='__main__':
    # 启动web服务器
    app.run()














