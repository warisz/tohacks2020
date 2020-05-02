from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class UserForm(FlaskForm):

    url = StringField('Website URL', validators = [DataRequired()])
    submit = SubmitField('Start')
