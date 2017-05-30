from  flask import Flask,render_template,session,redirect,url_for,flash
from  flask import make_response,request
from  flask_script import Manager
from  flask_bootstrap import Bootstrap
from  flask_moment import Moment
from  datetime import datetime
from  flask_wtf import FlaskForm
from  wtforms import StringField, SubmitField
from  wtforms.validators import Required
from  flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

app.config['SECRET_KEY'] = 'hard to guess string'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
	__tablename__='users'
	id=db.Column(db.Integer,primary_key=True)
	name=db.Column(db.String(64),unique=True)
	passwd=db.Column(db.String(64))
	enable=db.Column(db.Integer)
	
	def __repr__(self):
		return '<Role %r>' % self.name
class Task(db.Model):
	__tablename__='tasks'
	id=db.Column(db.Integer,primary_key=True)
	username=db.Column(db.String(64),unique=True,index=True)
	title=db.Column(db.String(64))
	body=db.Column(db.String(256))
	creattime=db.Column(db.timestamp)
	updatetime=db.Column(db.timestamp)
	state=db.Column(db.String(64))

 	
 	def __repr__(self):
		return '<Role %r>' % self.name

	# repsponse=make_response('<h1>this is the todolist index page!</h1>')
	# repsponse.set_cookie('answer','42')
	# user_agent=request.headers.get('user_Agent')
	# return '<p>your browser is %s </p>' %user_agent
# class NameForm(FlaskForm):
# 	name=StringField('what is your name',validators=[Required()])
# 	submit=SubmitField('submit')

@app.route('/',methods=['GET'])
def index():
	#name=None
	form=NameForm()
	if  form.validate_on_submit():
		#oldname=session.get('name')
		user=User.query.filter_by(username=form.name.data).first()
		if user is None:
			user = User(username=form.name.data)
			db.session.add(user)
			db.session.commit()
			session['know']=False
		else:
			session['know']=True
		session['name']=form.name.data
		form.name.data=''
		# if oldname is not None and oldname != form.name.data:
		# 	flash('looks like you hanve changed you name')

		#session['name']=form.name.data
		return redirect(url_for('index'))
	return render_template('index.html',form=form,name=session.get('name'),know=session.get('know',False))

@app.route('/user/<name>')
def user(name):
	return render_template('user.html',name=name)

if __name__ == "__main__":
	#app.run(debug=True)
	manager.run()