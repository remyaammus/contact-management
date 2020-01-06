import wtforms as forms
from flask_wtf import FlaskForm
from .validators import PhoneNumberValidator


class ContactCreateForm(FlaskForm):
    id = forms.IntegerField('Contact ID')
    first_name = forms.StringField('First Name', validators=[forms.validators.DataRequired()])
    last_name = forms.StringField('Last Name', validators=[forms.validators.DataRequired()])
    email = forms.StringField('Email', validators=[forms.validators.DataRequired(), forms.validators.Email()])
    phone_number = forms.StringField('Phone Number',
                                     validators=[forms.validators.DataRequired(), PhoneNumberValidator()])
    submit = forms.SubmitField('Create Contact')
