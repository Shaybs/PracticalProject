from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/', methods = ['POST'])
def get_test():
	return {"name":"Bob"}

@app.route('/post-test', methods=['POST'])
def post_test():
	account = request.get_json()["Account"]
	return {"Account":account}

if __name__ == '__main__':
	app.run(port=5002, host='0.0.0.0')