from flask.ext.mail import Message
from hello import mail
from app import mail, create_app
from flask import render_template
from config import ADMINS
from .model import User
from threading import Thread

app = create_app('default')


def send_async_email(app, msg):
	with app.app_context():
		mail.send(msg)


