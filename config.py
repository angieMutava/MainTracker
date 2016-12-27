import os

basedir = os.path.abspath(os.path.dirname(__file__))

ADMINS = ['mantenimiento.trackapp@gmail.com']

class Config:
	WTF_CSRF_ENABLED = True
	
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	SQLALCHEMY_TRACK_MODIFICATIONS = True
	SECRET_KEY = 'I choose to love you.'
	MAIL_SERVER = 'smtp.gmail.com'
	MAIL_PORT = 465
	MAIL_USE_SSL = True
	MAIL_USERNAME = 'mantenimiento.trackapp@gmail.com'
	MAIL_PASSWORD = 'mantenimiento'

	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig:
	DEBUG = True
	DEVELOPMENT = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
       'sqlite:///' + os.path.join(basedir, 'tracker.sqlite')

	@staticmethod
	def init_app(app):
		pass
   

class ProductionConfig:
	DEBUG = False

	@staticmethod
	def init_app(app):
		pass

config = {
	'development': DevelopmentConfig,
	'production': ProductionConfig,
	'default': DevelopmentConfig}
