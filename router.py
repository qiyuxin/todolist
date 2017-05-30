from flask import flask

app=flask(__name__)


@app.route('/users',methods='GET')
def  users():
	pass
@app.route('/tasks',methods='GET')
def  tasks():
	pass

@app.route('/users',methods='POST')
def  user-xj():
	pass
@app.route('/tasks',methods='POST')
def  task-xj():
	pass

@app.route('/users',id='id',methods='POST')
def  user-():
	pass
