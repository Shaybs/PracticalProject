from flask import abort, render_template, redirect, url_for, request, flash
from application import app
import requests

@app.route('/', methods=['GET'])
def test():
	requests.post('http://localhost:5001/post-test', json={"name":"Bob"})
	
	shuaib = requests.post('http://localhost:5002/post-test', json={"Country":"Britain"})
	if shuaib == True:
		pass
		#shuaib.json()
	return "OK\n"

@app.route('/post-test', methods=['POST'])
def post_test():
	country = request.get_json()["Country"]
	return "OK\n"