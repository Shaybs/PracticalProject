from flask import abort, render_template, redirect, url_for, request, flash
from application import app, db


@app.route('/', methods = ['GET'])
def get_test():
    return {"name":"Bob"}

@app.route('/post-test', methods=['POST'])
def post_test():
    print(request.json)
    return "OK\n"

@app.route('/home')
def home():
	return render_template('home.html', title='Home')

@app.route('/about')
def about():
	return render_template('about.html', title='About')