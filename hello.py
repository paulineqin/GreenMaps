from flask import Flask
app = Flask(__name__)

@app.route('/homepage')
def hello_world():
	f = open("Home.html", "r")
	contents = f.read()
	return contents

@app.route('/page2')
def hello_world_2():
	return 'Hello, world 2!'	