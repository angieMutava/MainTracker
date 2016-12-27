from . import auth
from .. import db
from ..model import User
from .form import SignInForm, SignUpForm
from flask.ext.login import login_user, logout_user, current_user, login_required
from flask import render_template, redirect, url_for, request, flash, session

@auth.route('/')
@auth.route('/sign_in', methods=['GET', 'POST'])
def signIn():
	user_form = SignInForm()
	if user_form.validate_on_submit():
		user = User.query.filter_by(username=user_form.username.data).first()
		if user is not None and user.verify_password(user_form.password.data):
			login_user(user, user_form.remember_me.data)
			return redirect(url_for('main.home_page'))
		flash("invalid username or password")
	return render_template('auth/login.html', user_form=user_form)

@auth.route('/sign_up', methods=['GET', 'POST'])
def signUp():
	user_form = SignUpForm()
	if user_form.validate_on_submit():
		user = User(firstname=user_form.firstname.data,
			        lastname=user_form.lastname.data,
			        email=user_form.email.data,
			        phone_number=user_form.phone_number.data,
			        username=user_form.username.data,
			        password=user_form.password.data)
		db.session.add(user)
		db.session.commit()
		flash("user registered successfully")
		return redirect(url_for('auth.signIn'))
	return render_template('auth/signup.html', user_form=user_form)
	
@auth.route('/sign_out')
def sign_out():
	logout_user()
	return redirect(url_for('auth.login'))

@auth.route('/reset', methods=['GET', 'POST'])
def reset_password():
	return render_template('forgot_password.html')		
