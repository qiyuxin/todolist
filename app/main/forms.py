from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..database import User,Task

class addTaskForm(FlaskForm):
	username = StringField('username', validators=[Required(), Length(1, 64)])
	title = StringField('title', validators=[Required(), Length(1, 64)])
	body = StringField('body', validators=[Required(), Length(1, 256)])
	state = StringField('state', validators=[Required(),Length(1, 64)])
	
	submit = SubmitField('submit')
	
	def validate_username(self, field):
		if not Task.query.filter_by(username=field.data).first():
			raise ValidationError('Username must be already in use.')

class addUserForm(FlaskForm):
	name = StringField('name', validators=[Required(), Length(1, 64)])
	passwd = PasswordField('passwd', validators=[Required(), Length(1, 64)])
	enable = StringField('enable', validators=[Required(), Length(1, 64)])
	
	
	submit = SubmitField('submit')
	
	def validate_name(self, filed):
		if User.query.filter_by(name=field.data).first():
			raise ValidationError('Username already in use.')