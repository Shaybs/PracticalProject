from flask import abort, render_template, redirect, url_for, request, flash
from application import app
import requests

@app.route('/test-5002', methods=['GET','POST'])
def test_account():	
	country = requests.post('http://account-service:5002/post-test', json={"Country":"Pakistan"})
	if country.ok:
		return country.json()["country"]
	return "OK\n"

@app.route('/test-5001', methods=['GET','POST'])
def test_country():
	name = requests.post('http://country-service:5001/post-test', json={"name":"Bob"})
	if name.ok:
		return name.json()["name"]
	return "OK\n"

@app.route('/post-test', methods=['POST'])
def post_test():
	country = request.get_json()["Country"]
	return {"response":country}