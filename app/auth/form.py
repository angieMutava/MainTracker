from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Email, Length, EqualTo, Regexp
from ..model import User
from wtforms import ValidationError

class SignInForm(Form):
	username = StringField('Username', validators=[Required(), Length(1, 64)])
	password = PasswordField('Password', validators=[Required()])
	remember_me = BooleanField('Keep me logged in')
	submit = SubmitField('Sign In')

class SignUpForm(Form):

	first_name = StringField('FirstName', validators=[Required(), Length(1, 20)])
	last_name = StringField('LastName', validators=[Required(), Length(1, 20)])
	email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
	phone_number = StringField('PhoneNumber', validators=[Required(), Length(1, 64)])
	username = StringField('Username', validators=[Required(), Length(1, 64), 
		Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 'Usernames must have only letters, ''numbers, dots or underscores')])
	password = PasswordField('Password', validators=[Required(), EqualTo('conf_password', message='Passwords must match.')])
	conf_password = PasswordField('Confirm password', validators=[Required()])
	submit = SubmitField('Sign Up')

	def validate_email(self, field):
		if User.query.filter_by(email=field.data).first():
			raise ValidationError('Email already registered.')

	def validate_username(self, field):
		if User.query.filter_by(username=field.data).first():
			raise ValidationError('Username already in use.')


class PasswordResetRequest(Form):
	email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
	submit = SubmitField('Reset Password')

class ChangePasswordForm(Form):
	old_password = PasswordField('Old password', validators=[Required()])
	password = PasswordField('New password', validators=[
        Required(), EqualTo('password2', message='Passwords must match')])
	password2 = PasswordField('Confirm new password', validators=[Required()])
	submit = SubmitField('Update Password')	

class PasswordResetForm(Form):
	email = StringField('Email', validators=[Required(), Length(1, 64),
                                             Email()])
	password = PasswordField('New Password', validators=[
        Required(), EqualTo('password2', message='Passwords must match')])
	password2 = PasswordField('Confirm password', validators=[Required()])
	submit = SubmitField('Reset Password')

	def validate_email(self, field):
		if User.query.filter_by(email=field.data).first() is None:
			raise ValidationError('Unknown email address.')	

class ChangeEmailForm(Form):
	email = StringField('New Email', validators=[Required(), Length(1, 64),
                                                 Email()])
	password = PasswordField('Password', validators=[Required()])
	submit = SubmitField('Update Email Address')	
