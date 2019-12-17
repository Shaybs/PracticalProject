from flask import Flask
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def test():
	requests.post('http://localhost:5001/post-test', json={"name":"Bob"})
	
	shuaib = requests.post('http://localhost:5002/post-test', json={"Country":"Britain"})
	if shuaib == True:
		pass
		#shuaib.json()
	return "OK\n"

if __name__== '__main__':
	app.run(host='0.0.0.0')