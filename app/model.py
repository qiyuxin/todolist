from . import db

class User(db.Model):
	__tablename__='users'
	id=db.Column(db.Integer,primary_key=True)
	name=db.Column(db.String(64),unique=True)
	passwd=db.Column(db.String(64))
	enable=db.Column(db.Integer)
	
	def __repr__(self):
		return '<User %r>' % self.name

class Task(db.Model):
	__tablename__='tasks'
	id=db.Column(db.Integer,primary_key=True)
	username=db.Column(db.String(64),unique=True,index=True)
	title=db.Column(db.String(64))
	body=db.Column(db.Text)
	ctime=db.Column(db.Time)
	state=db.Column(db.String(64))

 	
 	def __repr__(self):
		return '<Task %r>' % self.name
