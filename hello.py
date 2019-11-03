from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello_world():
	return '<strong>Hello, world!</strong>'

@app.route('/page2')
def hello_world_2():
	return 'Hello, world 2!'