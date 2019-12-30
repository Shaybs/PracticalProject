from flask import Flask, request
from application import app
import requests

@app.route('/', methods = ['GET', 'POST'])
def get_test():
	return {"name":"Bob"}

@app.route('/post-account', methods=['POST'])
def post_test():
	account = request.get_json()["Account"]
	return {"Account":account}