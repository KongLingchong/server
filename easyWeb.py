from flask import Flask,render_template,request,redirect
def renderWeb_notNum(html_name,route_):
    app = Flask(__name__)
    @app.route(route_)
    def index():
        return render_template('index.html')
    app.run()
def renderWeb_num(html_name,route_,num):
    app = Flask(__name__)
    @app.route(route_)
    def index():
        return render_template('index.html',n = num)
    app.run()
def getNum_notPost(name):
    num = request.values.get(name)
    return num
def getNum_render_post(html_name,route_,name):
    @app.route(route_,methods= ["POST"])
    def index():
        num = request.values.get(name)
        return render_template(html_name)
    return num
    app.run()
def renderWeb_redirect(url,route_):
    app = Flask(__name__)
    @app.route(route_)
    def index():
        return redirect(url)
    app.run()
