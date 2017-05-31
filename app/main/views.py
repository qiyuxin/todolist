# coding=utf-8
from flask import render_template,request,session,g,redirect,url_for,flash
from . import main
from .. import db
from .. import loginmanager
from ..database import db_session,User,Task
import time
# from .forms import NameForm
from flask_wtf import FlaskForm
from flask_login import login_user,login_required,current_user
#from flask.ctx import _request_ctx_stack
#form = FlaskForm()
# def data_in():
# 	session = db_session
# 	user_lisi = User(name='lisi', passwd='lisi123',enable=1)
# 	user_susan = User(name='susan', passwd='lisi123',enable=1)
# 	user_david = User(name='david', passwd='lisi123',enable=1)
# 	task_1 = Task(username='lisi',title='write',body='write zhoubao',createtime='time.Now()',updatetime='time.Now()',state='init')
# 	task_2 = Task(username='susan',title='dasao',body='dasao woshi',createtime='time.Now()',updatetime='time.Now()',state='doing')
# 	task_3 = Task(username='david',title='paobu',body='paobu zhoumo',createtime='time.Now()',updatetime='time.Now()',state='init')
# 	session.add(user_lisi,user_susan,user_david,task_1,task_2,task_3)
# 	session.commit()
# 	session.close()
# app_cxt = app.app_context()
# app_cxt.push()
# 通过用户名，获取用户记录，如果不存在，则返回None
def query_user(username):
	sn = db_session()
	x = sn.query(User.name, User.passwd, User.enable).filter_by(name=username).first()
	print "*****", x
	return x
 
# 如果用户名存在则构建一个新的用户类对象，并使用用户名作为ID
# 如果不存在，必须返回None
@loginmanager.user_loader
def load_user(username):
    usr = query_user(username)
    if usr is not None:
        curr_user = User()
        curr_user.id = username
        curr_user.is_authenticated = True
        curr_user.is_active = usr.enable > 0
        return curr_user


@main.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent

@main.route('/users',methods=["GET"])
@login_required
def users():
		sn=db_session()
		uusers=sn.query(User.name,User.passwd,User.enable).all()
		print "==========", uusers
		print "yyyyy", current_user
		return render_template('user.html',users=uusers)
	
@main.route('/tasks',methods=["GET"])
@login_required
def tasks():
    sv=db_session()
    tasks=sv.query(Task.username,Task.title,Task.body,Task.state).all()
    print "00000",tasks
    return render_template('task.html',tasks=tasks)

# @main.route('/login', methods=["GET"])
# def login():
# 	return render_template('login.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        user = query_user(username)
        # 验证表单中提交的用户名和密码
        if user is not None and request.form['password'] == user[1]:
            curr_user = User()
            curr_user.id = username
 
            # 通过Flask-Login的login_user方法登录用户
            login_user(curr_user)
 
            # 如果请求中有next参数，则重定向到其指定的地址，
            # 没有next参数，则重定向到"index"视图
            next = request.args.get('next')
            return redirect(next or '/users')
 
        flash('Wrong username or password!')
    # GET 请求
    return render_template('login.html')

#@main.route('/check_user', methods=["POST"])
# def check_user():
	#TODO: verify username and pwd
	#return redirect('/users', 302)








@main.route('/users',methods=["POST"])
def  user_xj():
	pass
@main.route('/tasks',methods=["POST"])
def  task_xj():
	pass

@main.route('/users',methods=["POST"])
def  user_it():
	pass
# 	str(User.query.filter_by(role=user_role))
# 'SELECT users.id AS users_id, users.username AS users_username,
# users.role_id AS users_role_id FROM users WHERE :param_1 = users.role_id'
