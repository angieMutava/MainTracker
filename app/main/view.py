from . import main
from flask import render_template
from .. import db
from ..model import Assigned, Maintanance, Repair, User  
from flask.ext.login import logout_user, current_user, login_required
from flask import render_template, redirect, url_for, request, flash, session
from .form import RepairForm, MaintananceForm, AssignForm, adminEditForm
from .decorators import required_roles


@main.route('/')
@main.route('/home')
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
@login_required
@required_roles(2)
def admin_home():
	maintanances = (Maintanance.query.filter_by(urgency='high').all())
	repairs = (Repair.query.filter_by(urgency='high').all())
	return render_template('admin/admin_home.html', maintanances=maintanances, repairs=repairs)


@main.route('/admin_mains', methods=['GET', 'POST'])
@login_required
@required_roles(2)
def admin_mains():
	maintanances = Maintanance.query.all()
	return render_template('admin/maintanance.html', maintanances=maintanances)


@main.route('/admin_repairs', methods=['GET', 'POST'])
@login_required
@required_roles(2)
def admin_repairs():
	repairs = Repair.query.all()
	return render_template('admin/repairs.html', repairs=repairs)


@main.route('/admin_users', methods=['GET', 'POST'])
@login_required
@required_roles(2)
def admin_users():
	users = User.query.all()
	return render_template('admin/users.html', users=users)


@main.route('/edit_users/<username>', methods=['GET', 'POST'])
@login_required
@required_roles(2)
def edit_users(username):
	user = User.query.filter_by(username=username).first()
	form = adminEditForm(user=user)
	if form.validate_on_submit():
		try:
			user.email = form.email.data
			user.first_name = form.first_name.data
			user.last_name = form.last_name.data
			user.phone_number = form.phone_number.data
			user.username = form.username.data
			db.session.add(user)
			db.session.commit()
			flash("The profile has been updated.")
			return redirect(url_for('main.admin_home'))
		except Exception, e:
			db.session.rollback()
			flash("An error occurred while updating user information")
			return redirect(url_for('main.edit_users', username=user.username))
	return render_template('admin/edit_user.html', form=form, user=user)
		

@main.route('/approve', methods=['GET', 'POST'])
@login_required
@required_roles(2)
def approve():
	return render_template('admin/approvereject.html')


@main.route('/assign', methods=['GET', 'POST'])
@login_required
@required_roles(2)
def assign():
	assign_form = AssignForm()
	if assign_form.validate_on_submit():
		assigned = Assigned(first_name=assign_form.first_name.data,
			last_name=assign_form.last_name.data,
			phone_number=assign_form.phone_number.data,
			issue=assign_form.issue.data,
			department=assign_form.department.data)
		db.session.add(assigned)
		db.session.commit()
		#token = user.generate_confirmation_token()
		#send_email(user.email, 'Confirm Your Account', 'auth/email/confirm', user=user, token=token)
		#flash('A confirmation email has been sent to your email.')
		return redirect(url_for('main.admin_home'))
	return render_template('admin/assign.html', assign_form=assign_form)
