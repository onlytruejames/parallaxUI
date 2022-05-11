import parallaxCompiler.parallaxCompiler as parallaxCompiler
from flask import Flask, render_template, request
import json, base64

app = Flask(__name__)

def cleanUp(string):
    return string.replace()

@app.route('/')
def index():
    data = request.cookies.get('data')
    data = base64.b64decode(data)
    data = data.decode('utf-8')
    return render_template('index.html', data=data)

@app.route('/screen/')
@app.route('/screen/')
def screen():
    data = request.cookies.get('data')
    data = base64.b64decode(data)
    data = data.decode('utf-8')
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