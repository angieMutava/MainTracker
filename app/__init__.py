from flask.ext.sqlalchemy import SQLAlchemy
from config import config
from flask import Flask
from flask.ext.login import LoginManager

app = Flask(__name__)

db = SQLAlchemy()
login_manager = LoginManager()
#can be set to basic ,None or strong
login_manager.session_protection = 'None'
#The login_view
#attribute sets the endpoint for the login page. Recall that because the login route is inside
#a blueprint, it needs to be prefixed with the blueprint name.
login_manager.login_view = 'auth.login'

def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)

	db.init_app(app)
	login_manager.init_app(app)