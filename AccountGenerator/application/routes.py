from flask import Flask, request
from application import app
import requests
import random

@app.route('/', methods = ['GET', 'POST'])
def get_test():
	return {"name" : "Bob"}

@app.route('/post-account', methods=['POST'])
def post_test():
	country = request.get_json()["Country"]
	if country == "Belarus":
		initial = "62"
		value = random.randint(1,9)
		value_string = str(value)
		response_value = initial + value_string
		return {"Account":response_value}