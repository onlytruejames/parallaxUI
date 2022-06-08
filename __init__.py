from ast import Num
import parallaxCompiler.parallaxCompiler as parallaxCompiler
from flask import Flask, render_template, request
import json, base64

def putCookieBackTogether(cookie: list) -> str:
    result = ""
    for subCookie in cookie:
        result += subCookie
    return base64.b64decode(result).decode('utf-8')

app = Flask(__name__)

@app.route('/')
def index():
    try:
        num = int(request.cookies.get('num'))
        print(num)
        cookies = []
        for i in range(num):
            cookies.append(request.cookies.get(f"c{i}"))
        data = putCookieBackTogether(cookies)
    except:
        data = "[]"
    return render_template('index.html', data=data)

@app.route('/screen/')
@app.route('/screen/')
def screen():
    try:
        num = int(request.cookies.get('num'))
        print(num)
        cookies = []
        for i in range(num):
            cookies.append(request.cookies.get(f"c{i}"))
        data = putCookieBackTogether(cookies)
    except:
        data = "[]"
    if not data:
        return "error"
    try:
        return parallaxCompiler.compile(json.loads(data))
    except:
        return "error"

@app.route('/getKeywords/')
def getKeywords():
    return json.dumps(parallaxCompiler.getKeywords())

@app.route('/getStrictKeywords/')
def getStrictKeywords():
    return json.dumps(parallaxCompiler.getStrictKeywords())

@app.route('/getSpecials/')
def getSpecials():
    return json.dumps(parallaxCompiler.getSpecials())

if __name__ == '__main__':
    app.run()