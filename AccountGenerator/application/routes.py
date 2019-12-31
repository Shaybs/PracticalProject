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
	if country == "Pakistan":
		initial = "60"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		value3 = random.randint(1,9)
		value3_string = str(value3)
		value4 = random.randint(1,9)
		value4_string = str(value4)
		response_value = initial + value1_string + value2_string + value3_string + value4_string
		return {"Account":response_value}
