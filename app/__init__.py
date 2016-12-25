from flask_sqlalchemy import SQLAlchemy
from config import config
from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail
from flask_bootstrap import Bootstrap


app = Flask(__name__)

db = SQLAlchemy()
login_manager = LoginManager()
mail = Mail()
bootstrap = Bootstrap()
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
	mail.init_app(app)
	bootstrap.init_app(app)

	from auth import auth as auth_blueprint
	app.register_blueprint(auth_blueprint)

	return app