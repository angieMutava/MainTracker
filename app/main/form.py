from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, SubmitField, SelectField, DateField
from wtforms.validators import Required, Length
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