from flask import Flask, request
from application import app
import requests
import random

numbers = '0123456789'

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
	card_cvc = requests.post('http://cvc-service:5006/post-cvc', json={"Country":country})
	cvc = card_cvc.json()["CVC"]
	card_cardnumber = requests.post('http://cardnumber-service:5005/post-cardnumber', json={"Country":country})
	cardnumber = card_cardnumber.json()["CardNumber"]
	card_sort = requests.post('http://sort-service:5004/post-sort', json={"Country":country})
	sort = card_sort.json()["Sort"]
	account = requests.post('http://account-service:5002/post-account-8', json={"Country":country})
	iban_account = account.json()["Account"]
	iban_preambleservice = requests.post('http://country-service:5001/post-iban-8', json={"Country":country})
	iban_preamble = iban_preambleservice.json()["IBAN"]
	iban_numbers_in_string = ''.join(random.choice(numbers) for i in range(12))
	iban = iban_preamble + iban_account + iban_numbers_in_string
	return {"IBAN":iban, "BankAccount":iban_account, "Sort":sort, "CardNumber":cardnumber, "CVC":cvc}

@app.route('/post-test', methods=['POST'])
def post_test():
	country = request.get_json()["Country"]
	return {"response":country}



