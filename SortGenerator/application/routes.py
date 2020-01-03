from flask import Flask, request
from application import app
import requests
import random

@app.route('/post-sort', methods=['POST'])
def post_sort():
	country = request.get_json()["Country"]
	if country == "Pakistan":
		initial = "70"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		response_value = initial + '-' + value1_string + '-' + value2_string
		return {"Sort":response_value}
	elif country == "Belarus":
		initial = "71"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		response_value = initial + '-' + value1_string + '-' + value2_string
		return {"Sort":response_value}
	elif country == "United Kingdom":
		initial = "72"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		response_value = initial + '-' + value1_string + '-' + value2_string
		return {"Sort":response_value}
	elif country == "United Arab Emirates":
		initial = "73"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		response_value = initial + '-' + value1_string + '-' + value2_string
		return {"Sort":response_value}
	elif country == "South Korea":
		initial = "74"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		response_value = initial + '-' + value1_string + '-' + value2_string
		return {"Sort":response_value}
	elif country == "Italy":
		initial = "75"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		response_value = initial + '-' + value1_string + '-' + value2_string
		return {"Sort":response_value}
	elif country == "China":
		initial = "76"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		response_value = initial + '-' + value1_string + '-' + value2_string
		return {"Sort":response_value}
	elif country == "India":
		initial = "77"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		response_value = initial + '-' + value1_string + '-' + value2_string
		return {"Sort":response_value}
	elif country == "Singapore":
		initial = "77"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		response_value = initial + '-' + value1_string + '-' + value2_string
		return {"Sort":response_value}
	elif country == "Denmark":
		initial = "78"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		response_value = initial + '-' + value1_string + '-' + value2_string
		return {"Sort":response_value}
	elif country == "Switzerland":
		initial = "79"
		value1 = random.randint(1,9)
		value1_string = str(value1)
		value2 = random.randint(1,9)
		value2_string = str(value2)
		response_value = initial + '-' + value1_string + '-' + value2_string
		return {"Sort":response_value}

