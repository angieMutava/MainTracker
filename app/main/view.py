from . import main
from flask import render_template


@main.route('/home', methods=['GET', 'POST'])
def home_page():
	return render_template('home.html')