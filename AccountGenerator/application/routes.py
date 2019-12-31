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
		value1_string = str(value)
		value2 = random.randint(1,9)
		value2_string = str(value)
		value3 = random.randint(1,9)
		value3_string = str(value)
		value4 = random.randint(1,9)
		value4_string = str(value)
		response_value = initial + value1_string + value2_string + value3_string + value4_string
		return {"Account":response_value}
	elif country == "Belarus":
		initial = "61"
		value1 = random.randint(1,9)
		value1_string = str(value)
		value2 = random.randint(1,9)
		value2_string = str(value)
		value3 = random.randint(1,9)
		value3_string = str(value)
		value4 = random.randint(1,9)
		value4_string = str(value)
		response_value = initial + value1_string + value2_string + value3_string + value4_string
		return {"Account":response_value}
	elif country == "United Kingdom":
		initial = "62"
		value1 = random.randint(1,9)
		value1_string = str(value)
		value2 = random.randint(1,9)
		value2_string = str(value)
		value3 = random.randint(1,9)
		value3_string = str(value)
		value4 = random.randint(1,9)
		value4_string = str(value)
		response_value = initial + value1_string + value2_string + value3_string + value4_string
		return {"Account":response_value}
	elif country == "United Arab Emirates":
		initial = "63"
		value1 = random.randint(1,9)
		value1_string = str(value)
		value2 = random.randint(1,9)
		value2_string = str(value)
		value3 = random.randint(1,9)
		value3_string = str(value)
		value4 = random.randint(1,9)
		value4_string = str(value)
		response_value = initial + value1_string + value2_string + value3_string + value4_string
		return {"Account":response_value}
	elif country == "South Korea":
		initial = "64"
		value1 = random.randint(1,9)
		value1_string = str(value)
		value2 = random.randint(1,9)
		value2_string = str(value)
		value3 = random.randint(1,9)
		value3_string = str(value)
		value4 = random.randint(1,9)
		value4_string = str(value)
		response_value = initial + value1_string + value2_string + value3_string + value4_string
		return {"Account":response_value}
	elif country == "Italy":
		initial = "65"
		value1 = random.randint(1,9)
		value1_string = str(value)
		value2 = random.randint(1,9)
		value2_string = str(value)
		value3 = random.randint(1,9)
		value3_string = str(value)
		value4 = random.randint(1,9)
		value4_string = str(value)
		response_value = initial + value1_string + value2_string + value3_string + value4_string
		return {"Account":response_value}
	elif country == "China":
		initial = "66"
		value1 = random.randint(1,9)
		value1_string = str(value)
		value2 = random.randint(1,9)
		value2_string = str(value)
		value3 = random.randint(1,9)
		value3_string = str(value)
		value4 = random.randint(1,9)
		value4_string = str(value)
		response_value = initial + value1_string + value2_string + value3_string + value4_string
		return {"Account":response_value}
	elif country == "India":
		initial = "67"
		value1 = random.randint(1,9)
		value1_string = str(value)
		value2 = random.randint(1,9)
		value2_string = str(value)
		value3 = random.randint(1,9)
		value3_string = str(value)
		value4 = random.randint(1,9)
		value4_string = str(value)
		response_value = initial + value1_string + value2_string + value3_string + value4_string
		return {"Account":response_value}
	elif country == "Singapore":
		initial = "67"
		value1 = random.randint(1,9)
		value1_string = str(value)
		value2 = random.randint(1,9)
		value2_string = str(value)
		value3 = random.randint(1,9)
		value3_string = str(value)
		value4 = random.randint(1,9)
		value4_string = str(value)
		response_value = initial + value1_string + value2_string + value3_string + value4_string
		return {"Account":response_value}
	elif country == "Denmark":
		initial = "68"
		value1 = random.randint(1,9)
		value1_string = str(value)
		value2 = random.randint(1,9)
		value2_string = str(value)
		value3 = random.randint(1,9)
		value3_string = str(value)
		value4 = random.randint(1,9)
		value4_string = str(value)
		response_value = initial + value1_string + value2_string + value3_string + value4_string
		return {"Account":response_value}
	elif country == "Switzerland":
		initial = "69"
		value1 = random.randint(1,9)
		value1_string = str(value)
		value2 = random.randint(1,9)
		value2_string = str(value)
		value3 = random.randint(1,9)
		value3_string = str(value)
		value4 = random.randint(1,9)
		value4_string = str(value)
		response_value = initial + value1_string + value2_string + value3_string + value4_string
		return {"Account":response_value}
