from flask import abort, render_template, redirect, url_for, request, flash
from application import app

#Render the home page
@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', title='Home')

#Render the about page
@app.route('/about')
def about():
	return render_template('about.html', title='About')

#Render the test page
@app.route('/test', methods = ['GET'])
def get_test():
    return {"name":"Bob"}

#Render the post-test page
@app.route('/post-test', methods=['POST'])
def post_test():
    print(request.json)
    return "OK\n"

@app.route('/new-test', methods=['GET'])
def test():
	requests.post('http://localhost:5001/post-test', json={"name":"Bob"})
	
	country = requests.post('http://central-service:5000/post-test', json={"Country":"Britain"})
	if country == True:
		pass
		#shuaib.json()
	return "OK\n"