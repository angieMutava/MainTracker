from . import main
from flask import render_template
from .. import db
from ..model import User, Repair, Maintanance
from flask.ext.login import logout_user, current_user, login_required
from flask import render_template, redirect, url_for, request, flash, session
from .form import RepairForm, MaintananceForm
from .decorators import required_roles


@main.route('/')
@main.route('/home', methods=['GET', 'POST'])
def home_page():
	return render_template('home.html')


@main.route('/index_page', methods=['GET', 'POST'])
@login_required
def index():
	repairs = (Repair.query.filter_by(raised_by=current_user.username))
	maintanances = (Maintanance.query.filter_by(raised_by=current_user.username))
	return render_template('base.html', repairs=repairs, maintanances=maintanances)


@main.route('/repair', methods=['GET', 'POST'])
@login_required
def repair():
	repair_form = RepairForm()
	if repair_form.validate_on_submit():
		repair = Repair(item_name=repair_form.item_name.data,
			item_issue=repair_form.item_issue.data,
			item_type=repair_form.item_type.data,
			urgency=repair_form.urgency.data,
			raised_by=current_user.username)
		db.session.add(repair)
		db.session.commit()
		flash("Repair request submitted successfully")
		return redirect(url_for('main.index'))
	return render_template('repair.html', repair_form=repair_form)


@main.route('/maintanance', methods=['GET', 'POST'])
@login_required
def maintanance():
	main_form = MaintananceForm()
	if main_form.validate_on_submit():
		main = Maintanance(item_name=main_form.item_name.data,
			item_issue=main_form.item_issue.data,
			item_type=main_form.item_type.data,
			urgency=main_form.urgency.data,
			raised_by=current_user.username)
		db.session.add(main)
		db.session.commit()
		flash("Maintanance request submitted successfully")
		return redirect(url_for('main.index'))
	return render_template('maintanance.html', main_form=main_form)


@main.route('/admin_home', methods=['GET', 'POST'])
@required_roles(2)
@login_required
def admin_home():
	maintanances = (Maintanance.query.filter_by(urgency='high').all())
	repairs = (Repair.query.filter_by(urgency='high').all())
	return render_template('admin/admin_home.html', maintanances=maintanances, repairs=repairs)


@main.route('/admin_mains', methods=['GET', 'POST'])
@required_roles(2)
@login_required
def admin_mains():
	maintanances = Maintanance.query.all()
	return render_template('admin/maintanance.html', maintanances=maintanances)


@main.route('/admin_repairs', methods=['GET', 'POST'])
@required_roles(2)
@login_required
def admin_repairs():
	repairs = Repair.query.all()
	return render_template('admin/repairs.html', repairs=repairs)


@main.route('/admin_users', methods=['GET', 'POST'])
@required_roles(2)
@login_required
def admin_users():
	users = User.query.all()
	return render_template('admin/users.html', users=users)
