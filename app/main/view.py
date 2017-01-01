from . import main
from flask import render_template
from .. import db
from ..model import User, Repair, Maintanance
from flask.ext.login import logout_user, current_user, login_required
from flask import render_template, redirect, url_for, request, flash, session
from .form import RepairForm, MaintananceForm


@main.route('/')
@main.route('/home', methods=['GET', 'POST'])
def home_page():
	return render_template('home.html')


@main.route('/index_page', methods=['GET', 'POST'])
def index():
	return render_template('base.html')


@main.route('/repair', methods=['GET', 'POST'])
def repair():
	repair_form = RepairForm()
	if repair_form.validate_on_submit():
		repair = Repair(item_name=repair_form.item_name.data,
			item_issue=repair_form.item_issue.data,
			item_type=repair_form.item_type.data,
			date_of_request=repair_form.date_of_request.data,
			urgency=repair_form.urgency.data,
			raised_by=current_user._get_current_object())
		db.session.add(repair)
		db.session.commit()
		flash("Repair request submitted successfully")
		return redirect(url_for('main.index'))
	return render_template('repair.html', repair_form=repair_form)


@main.route('/maintanance', methods=['GET', 'POST'])
def maintanance():
	main_form = MaintananceForm()
	if main_form.validate_on_submit():
		main = Repair(item_name=main_form.item_name.data,
			item_issue=main_form.item_issue.data,
			item_type=main_form.item_type.data,
			date_of_request=main_form.date_of_request.data,
			urgency=main_form.urgency.data,
			raised_by=current_user._get_current_object())
		db.session.add(main)
		db.session.commit()
		flash("Maintanance request submitted successfully")
		return redirect(url_for('main.index'))
	return render_template('maintanance.html', main_form=main_form)