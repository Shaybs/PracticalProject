from flask import abort, render_template, redirect, url_for, request, flash
from application import app


@app.route('/', methods=['GET'])
def test():
	requests.post('http://localhost:5001/post-test', json={"name":"Bob"})
	
	shuaib = requests.post('http://localhost:5002/post-test', json={"Country":"Britain"})
	if shuaib == True:
		pass
		#shuaib.json()
	return "OK\n"