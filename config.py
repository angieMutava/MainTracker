import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	WTF_CSRF_ENABLED = True
	SECRET_KEY = 'I choose to love you'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig:
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
'sqlite:///' + os.path.join(basedir, 'tracker.sqlite')

config = {
			'development': DevelopmentConfig,
			'default':DevelopmentConfig
	      }
