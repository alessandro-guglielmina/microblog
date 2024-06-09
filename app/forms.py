from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, Booleanfield, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember_me = Booleanfield('Remember Me')
	submit = SubmitField('Sign In')