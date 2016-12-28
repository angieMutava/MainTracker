from . import main
from flask import render_template


@main.route('/')
@main.route('/home', methods=['GET', 'POST'])
def home_page():
	return render_template('home.html')


@main.route('/index_page', methods=['GET', 'POST'])
def index():
	return render_template('base.html')