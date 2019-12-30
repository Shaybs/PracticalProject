from flask import Flask, request
from application import app
import requests

@app.route('/test-5002', methods=['GET','POST'])
def test_account():	
	account = requests.post('http://account-service:5002/post-account', json={"Account":6667})
	if account.ok:
		return account.json()["Account"]
	return "OK\n"

@app.route('/test-5001', methods=['GET','POST'])
def test_country():
	country = requests.post('http://country-service:5001/post-test', json={"Country":"Belarus"})
	if country.ok:
		return country.json()["Country"]
	return "OK\n"

@app.route('/post-test', methods=['POST'])
def post_test():
	country = request.get_json()["Country"]
	return {"response":country}