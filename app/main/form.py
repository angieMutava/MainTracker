from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, SubmitField, SelectField, DateField, TextAreaField
from wtforms.validators import Required, Length, Email, Regexp
from ..model import User, Maintanance, Repair
from wtforms import ValidationError
from wtforms.fields.html5 import DateField


class RepairForm(Form):
    item_name = StringField('Item Name', validators=[Required(), Length(1, 20)])
    item_issue = StringField('Item Issue', validators=[Required(), Length(1, 20)])
    item_type = StringField('Item Type', validators=[Required(), Length(1, 20)])
    urgency = SelectField(
        'Urgency',
        choices=[('high', 'High'), ('intermediate', 'Intermediate'), ('low', 'Low')]
    )
    submit = SubmitField('Report')


class MaintananceForm(Form):
    item_name = StringField('Item Name', validators=[Required(), Length(1, 20)])
    item_issue = StringField('Item Issue', validators=[Required(), Length(1, 20)])  
    item_type = StringField('Item Type', validators=[Required(), Length(1, 20)])
    urgency = SelectField(
        'Urgency',
        choices=[('high', 'High'), ('intermediate', 'Intermediate'), ('low', 'Low')]
    )
    submit = SubmitField('Report')


class ApproveRejectForm(Form):
    item_name = StringField('Item Name', validators=[Required(), Length(1, 20)])
    item_issue = StringField('Item Issue', validators=[Required(), Length(1, 20)])
    item_type = StringField('Item Type', validators=[Required(), Length(1, 20)])
    urgency = SelectField(
        'Urgency',
        choices=[('high', 'High'), ('intermediate', 'Intermediate'), ('low', 'Low')]
    )
    approvrej = SelectField(
        'ApproveReject',
        choices=[('approve', 'Approve'), ('reject', 'Reject')]
    )
    comment = TextAreaField("Comment", validators=[Required()])
    submit = SubmitField('Reject/Approve')


class AssignForm(Form):
    first_name = StringField('FirstName', validators=[Required(), Length(1, 20)])
    last_name = StringField('LastName', validators=[Required(), Length(1, 20)])
    phone_number = StringField('PhoneNumber', validators=[Required(), Length(1, 20)])
    issue = StringField('Issue', validators=[Required(), Length(1, 20)])
    department = SelectField(
        'Maintanance',
        choices=[('furniture', 'Furniture'), ('glass', 'Glass'), ('metal', 'Metal')]
    )
    submit = SubmitField('Assign')


class adminEditForm(Form):
    first_name = StringField('FirstName', validators=[Required(), Length(1, 20)])
    last_name = StringField('LastName', validators=[Required(), Length(1, 20)])
    email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
    phone_number = StringField('PhoneNumber', validators=[Required(), Length(1, 64)])
    username = StringField('Username', validators=[Required(), Length(1, 64), 
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 'Usernames must have only letters, ''numbers, dots or underscores')])
    submit = SubmitField('Edit')

    def validate_email(self, field):
        if field.data != self.user.email and User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if field.data != self.user.username and User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')
