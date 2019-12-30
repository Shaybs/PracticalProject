from flask import request
from application import app
import requests

@app.route('/', methods = ['POST'])
def get_test():
	return {"name":"Bob"}

@app.route('/post-test', methods=['POST'])
def post_test():
	account = request.get_json()["Account"]
	return {"Account":account}