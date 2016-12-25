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

def send_mail(subject, sender, recipients, text_body, html_body):
	msg = Message(subject, sender=sender, recipients=recipients)
	msg.body = text_body
	msg.html = html_body
	thr = Thread(target=send_async_email, args=[app, msg])
	thr.start()
	return thr


def notify_user(issues):
	send_mail('%s' % issues.title,
		       ADMINS[0],
		       [issues.raised_by.email],
		       render_template("send_mail.txt",
		       					issues=issues),
		       render_template("send_mail.html",
		       					issues=issues))

def assign_issue(issues):
	send_mail('%s' % issues.title,
		       ADMINS[0],
		       [issues.assigned_to],
		       render_template("send_mail_assign.txt",
		       					issues=issues),
		       render_template("send_mail_assign.html", issues=issues))

