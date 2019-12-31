from flask import Flask, request
from application import app
import requests

@app.route('/get-account6', methods=['GET','POST'])
def test_account6():	
	account = requests.post('http://account-service:5002/post-account-6', json={"Country":"Pakistan"})
	if account.ok:
		return account.json()["Account"]
	return "OK\n"

@app.route('/get-account8', methods=['GET','POST'])
def test_account8():	
	account = requests.post('http://account-service:5002/post-account-8', json={"Country":"Pakistan"})
	if account.ok:
		return account.json()["Account"]
	return "OK\n"

@app.route('/get-iban4', methods=['GET','POST'])
def test_iban4():
	iban = requests.post('http://country-service:5001/post-iban-4', json={"Country":"Belarus"})
	if iban.ok:
		return iban.json()["IBAN"]
	return "OK\n"

@app.route('/get-iban8', methods=['GET','POST'])
def test_iban8():
	iban = requests.post('http://country-service:5001/post-iban-8', json={"Country":"Belarus"})
	if iban.ok:
		return iban.json()["IBAN"]
	return "OK\n"

@app.route('/post-iban', methods=['POST'])
def post_iban():
	country = request.get_json()["Country"]
	account = requests.post('http://account-service:5002/post-account-8', json={"Country":country})
	iban_account = account.json()["Account"]
	iban = requests.post('http://country-service:5001/post-iban-8', json={"Country":country})
	iban_preamble = iban.json()["IBAN"]
	iban = iban_preamble + iban_account
	return {"IBAN":iban}

@app.route('/post-test', methods=['POST'])
def post_test():
	country = request.get_json()["Country"]
	return {"response":country}



