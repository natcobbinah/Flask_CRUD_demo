from flask_wtf import FlaskForm
from wtforms import StringField, DateField, RadioField, SubmitField
from wtforms.validators import DataRequired


gender_choices = (
    ("Male", "Male"),
    ("Female", "Female"),
)


class PatientForm(FlaskForm):
    FirstName = StringField('FirstName', validators=[DataRequired()])
    LastName = StringField('LastName', validators=[DataRequired()])
    DOB = DateField('Date Of Birth', validators=[DataRequired()])
    Gender = RadioField('Gender', choices=gender_choices)
    ContactNumber = StringField('ContactNumber', validators=[DataRequired()])
    Address = StringField('Address', validators=[DataRequired()])
    submit = SubmitField(label='Save')
