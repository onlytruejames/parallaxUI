import parallaxCompiler.parallaxCompiler as parallaxCompiler
from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/screen/', defaults = {"data": None})
@app.route('/screen/<data>/')
def screen(data):
    data = request.args.get('data')
    if not data:
        return "Error"
    return parallaxCompiler.compile(json.loads(data))

if __name__ == '__main__':
    app.run()