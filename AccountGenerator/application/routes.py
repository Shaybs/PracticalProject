from flask import Flask, request
from application import app
import requests
import random

@app.route('/', methods = ['GET', 'POST'])
def get_test():
	return {"name" : "Bob"}

@app.route('/post-account', methods=['POST'])
def post_test():
	account = request.get_json()["Account"]
	value = random.randint(1,9)
	value_string = str(value)
	return {"Account":value_string}