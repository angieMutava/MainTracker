from . import auth
from .. import db
from..email import send_email
from ..model import User
from .form import SignInForm, SignUpForm, PasswordResetForm, ChangePasswordForm, PasswordResetRequest, ChangeEmailForm
from flask.ext.login import login_user, logout_user, current_user, login_required
from flask import render_template, redirect, url_for, request, flash, session


@auth.route('/sign_in', methods=['GET', 'POST'])
def signIn():
	user_form = SignInForm()
	if user_form.validate_on_submit():
		user = User.query.filter_by(username=user_form.username.data).first()
		if user is not None and user.verify_password(user_form.password.data):
			login_user(user, user_form.remember_me.data)
			if current_user.role_id == 1:
				return redirect(request.args.get('next') or url_for('main.index'))
			else:
				return redirect(request.args.get('next') or url_for('main.admin_home'))	
		flash("Invalid username or password")
	return render_template('auth/login.html', user_form=user_form)


@auth.route('/sign_up', methods=['GET', 'POST'])
def signUp():
	user_form = SignUpForm()
	if user_form.validate_on_submit():
		user = User(first_name=user_form.first_name.data,
			last_name=user_form.last_name.data,
			email=user_form.email.data,
			phone_number=user_form.phone_number.data,
			username=user_form.username.data,
			password=user_form.password.data,
			role_id=1)
		db.session.add(user)
		db.session.commit()
		#token = user.generate_confirmation_token()
		#send_email(user.email, 'Confirm Your Account', 'auth/email/confirm', user=user, token=token)
		#flash('A confirmation email has been sent to your email.')
		return redirect(url_for('auth.signIn'))
	return render_template('auth/signup.html', user_form=user_form)
	

@auth.route('/sign_out')
def sign_out():
	logout_user()
	return redirect(url_for('auth.signIn'))


@auth.route('/reset', methods=['GET', 'POST'])
def reset_password():
	if not current_user.is_anonymous:
		return redirect(url_for('main.index'))
	user_form = PasswordResetForm()
	if user_form.validate_on_submit():
		user = User.query.filter_by(email=user_form.email.data).first()
		if user:
			token = user.generate_reset_token()
			send_email(user.email, 'Reset Your Password',
                       'auth/email/reset_password',
                       user=user, token=token,
                       next=request.args.get('next'))
			flash('An email with instructions to reset your password has been sent to you.')
			return redirect(url_for('auth.signIn'))
	return render_template('reset_password.html', user_form=user_form)

@auth.route('/reset/<token>', methods=['GET', 'POST'])
def password_reset(token):
	if not current_user.is_anonymous:
		return redirect(url_for('main.home_page'))
	form = PasswordResetForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user is None:
			return redirect(url_for('main.home_page'))
			if user.reset_password(token, form.password.data):
				flash('Your password has been updated.')
				return redirect(url_for('auth.signIn'))
			else:
				return redirect(url_for('main.home_page'))
	return render_template('reset_password.html', form=form)	


@auth.route('/confirm/<token>')
@login_required
def confirm(token):
	if current_user.confirmed:
		return redirect(url_for('main.home_page'))
	if current_user.confirm(token):
		flash('You have confirmed your account. Thanks!')
	else:
		flash('The confirmation link is invalid or has expired.')
	return redirect(url_for('auth.signIn'))
	

@auth.route('/unconfirmed')
def unconfirmed():
	if current_user.is_anonymous() or current_user.confirmed:
		return redirect('main.home_page')
	return render_template('auth/unconfirmed.html')


@auth.route('/confirm')
@login_required
def resend_confirmation():
	token = current_user.generate_confirmation_token()
	send_email('auth/email/confirm',
		'Confirm Your Account', user, token=token)
	flash('A new confirmation email has been sent to you by email.')
	return redirect(url_for('main.home_page'))								


@auth.before_app_request
def before_request():
	pass
	#if current_user.is_authenticated() and not current_user.confirmed and request.endpoint[:5] != 'auth.':
		#return redirect(url_for('auth.unconfirmed'))
	