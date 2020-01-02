from flask import abort, render_template, redirect, url_for, request, flash
from application.forms import RegistrationForm
from application.models import Users
from application import app
import requests

#Render the home page
@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', title='Home')

#Render the about page
@app.route('/about')
def about():
	return render_template('about.html', title='About')

#Render the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	return render_template('login.html', title='Login', form=form)

#Render the Registration
@app.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('home'))

	form = RegistrationForm()
	if form.validate_on_submit():
		hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

		user = Users(
			first_name=form.first_name.data,
			last_name=form.last_name.data,
			username=form.username.data,
			email=form.email.data,
			password=hashed_pw
		)

		db.session.add(user)
		db.session.commit()
		flash('You have successfully registered! You can now login')
		return redirect(url_for('login'))

	return render_template('register.html', title='Register', form=form)

#Render the test page
@app.route('/test', methods = ['GET'])
def get_test():
	return {"name":"Bob"}

#Render the post-test page
@app.route('/post-test', methods=['POST'])
def post_test():
	print(request.json)
	return "OK\n"

@app.route('/new-test', methods=['GET', 'POST'])
def test():
	#requests.post('http://central-service:5000/post-test', json={"name":"Bob"})
	iban = requests.post('http://central-service:5000/post-test', json={"Country":"Pakistan"})
	if iban.ok:
		return iban.json()["IBAN"]
		#shuaib.json()
	return "OK\n"

@app.route('/new-iban', methods=['GET', 'POST'])
def iban():
	iban = requests.post('http://central-service:5000/post-iban', json={"Country":"Pakistan"})
	if iban.ok:
		return iban.json()["IBAN"]
	return "OK\n"
