from flask import Flask, request
from application import app
import requests

@app.route('/', methods = ['GET', 'POST'])
def get_test():
	return {"name":"Bob"}

@app.route('/post-test', methods=['POST'])
def post_test():
	country = request.get_json()["Country"]
	return {"Country":country}