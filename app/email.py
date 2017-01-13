from flask.ext.mail import Message
from app import mail, create_app
from flask import render_template
from config import ADMINS
from .model import User
from threading import Thread

app = create_app('default')


def send_async_email(app, msg):
	with app.app_context():
		mail.send(msg)


def send_email(subject, sender, recipients, body, html, **kwargs):
	msg = Message(subject, sender=sender, recipients=recipients)
	msg.body = body
	msg.html = html
	thr = Thread(target=send_async_email, args=[app, msg])
	thr.start()
	return thr