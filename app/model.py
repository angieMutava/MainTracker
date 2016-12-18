from flask.ext.login import UserMixin
from . import login_manager
from . import db, login_manager

class User(UserMixin, db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(64))
	last_name = db.Column(db.String(64))
	email = db.Column(db.String(64), unique=True, index=True)
	phone_number = db.Column(db.String(64))
	username = db.Column(db.String(64), unique=True, index=True)
	password_hash = db.Column(db.String(128))

	@login_manager.user_loader
	def load_user(user_id):
		return User.query.get(int(user_id))	