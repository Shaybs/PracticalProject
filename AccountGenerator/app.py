from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def get_test():
	return {"name":"Bob"}

@app.route('/post-test', methods=['POST'])
def post_test():
	country = request.json()["Country"]
	return "OK\n"

if __name__ == '__main__':
	app.run(port=5002, host='0.0.0.0')