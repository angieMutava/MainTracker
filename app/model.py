from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask.ext.login import UserMixin
from datetime import datetime
from flask import current_app
from . import login_manager
from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(64))
	last_name = db.Column(db.String(64))
	email = db.Column(db.String(64), unique=True, index=True)
	phone_number = db.Column(db.String(64))
	username = db.Column(db.String(64), unique=True, index=True)
	password_hash = db.Column(db.String(128))
	role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
	confirm = db.Column(db.Boolean, default=False)
	#repair = db.relationship('Repair', backref='raised_by', lazy='immediate')
	#main = db.relationship('Maintanance', backref='raised_by', lazy='immediate')

	@login_manager.user_loader
	def load_user(user_id):
		return User.query.get(int(user_id))

	@property
	def password(self):
		raise AttributeError('password is not a readable attribute')

	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)

	def generate_confirmation_token(self, expiration=3600):
		s = Serializer(current_app.config['SECRET_KEY'], expiration)
		return s.dumps({'confirm': self.id})

	def confirm(self, token):
		s = Serializer(current_app.config['SECRET_KEY'])
		try:
			data = s.loads(token)
		except:
			return False
		if data.get('confirm') != self.id:
			return False
		self.confirmed = True
		db.session.add(self)
		return True


class Maintanance(db.Model):
	__tablename__ = 'mains'
	id = db.Column(db.Integer, primary_key=True)
	item_name = db.Column(db.String(64))
	item_issue = db.Column(db.String(64))
	item_type = db.Column(db.String(64))
	urgency = db.Column(db.String(64))
	raised_by = db.Column(db.String(64))


class Repair(db.Model):
	__tablename__ = 'repairs'
	id = db.Column(db.Integer, primary_key=True)
	item_name = db.Column(db.String(64))
	item_issue = db.Column(db.String(64))
	item_type = db.Column(db.String(64))
	urgency = db.Column(db.String(64))
	raised_by = db.Column(db.String(64))

class Role(db.Model):
	__tablename__ = 'roles'
	id = db.Column(db.Integer(), primary_key=True)
	name = db.Column(db.String(80), unique=True)
	description = db.Column(db.String(255))
	users = db.relationship('User', backref='role', lazy='dynamic')

	# __unicode__ is required by Flask-Admin, so we can have human-readable values for the Role when editing a User.
	# If we were using Python 3.0, this would be __str__ instead.
	def __unicode__(self):
		return self.name

	# __hash__ is required to avoid the exception TypeError: unhashable type: 'Role' when saving a User
	def __hash__(self):
		return hash(self.name)


class Assigned(db.Model):
	__tablename__ = 'assigns'
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(64))
	last_name = db.Column(db.String(64))
	phone_number = db.Column(db.String(64))
	issue = db.Column(db.String(64))
	department = db.Column(db.String(64))
	
