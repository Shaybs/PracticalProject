from flask import abort, render_template, redirect, url_for, request, flash
from application import app, db, bcrypt, login_manager
from application.models import Users
from application.forms import RegistrationForm, UpdateAccountForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/', methods = ['GET'])
def get_test():
    return {"name":"Bob"}

@app.route('/post-test', methods=['POST'])
def post_test():
    print(request.json)
    return "OK\n"

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', title='Home')

@app.route('/about')
def about():
	return render_template('about.html', title='About')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
            user=Users.query.filter_by(email=form.email.data).first()

            if user and bcrypt.check_password_hash(user.password, form.password.data):
                    login_user(user, remember=form.remember.data)
                    next_page = request.args.get('next')

                    if next_page:
                            return redirect(next_page)
                    else:
                            flash('Invalid email or password')
                            return redirect(url_for('home'))
                    
    return render_template('login.html', title='Login', form=form)

@login_manager.user_loader
def load_user(id):
        return Users.query.get(int(id))

@app.route('/logout')
@login_required
def logout():
        logout_user()
        return redirect(url_for('login'))

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
                        email=form.email.data,
                        password=hashed_pw
                )
                
                db.session.add(user)
                db.session.commit()
                flash('You have successfully registered! You can now login')
                return redirect(url_for('login'))
        return render_template('register.html', title='Register', form=form)

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
	form = UpdateAccountForm()

	if form.validate_on_submit():
		current_user.first_name = form.first_name.data
		current_user.last_name = form.last_name.data
		current_user.email = form.email.data
		db.session.commit()
		return redirect(url_for('account'))
	elif request.method == 'GET':
		form.first_name.data = current_user.first_name
		form.last_name.data = current_user.last_name
		form.email.data = current_user.email
	return render_template('account.html', title='Account', form=form)


