from flask import Flask
import flaskBGR as bgr
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hello')
def test():
	return 'test'

@app.route('/bgr')
def rgb():
	color = bgr.myFunction()

	return "hello %s"%color
