from flask import Flask, send_from_directory
import os
app = Flask(__name__)

@app.route('/homepage')
def hello_world():
	f = open("Home.html", "r")
	contents = f.read()
	return contents

@app.route('/page2')
def hello_world_2():
	return 'Hello, world 2!'	


@app.route('/img/<filename>')
def static_proxy_img(filename):
	root_dir = os.path.dirname(os.getcwd())
	serve_dir = os.path.join(root_dir, 'GreenMaps/img')
	return send_from_directory(serve_dir, filename)

@app.route('/css/<filename>')
def static_proxy_css(filename):
	root_dir = os.path.dirname(os.getcwd())
	serve_dir = os.path.join(root_dir, 'GreenMaps/css')
	return send_from_directory(serve_dir, filename)

@app.route('/fonts/<filename>')
def static_proxy_fonts(filename):
	root_dir = os.path.dirname(os.getcwd())
	serve_dir = os.path.join(root_dir, 'GreenMaps/fonts')
	return send_from_directory(serve_dir, filename)