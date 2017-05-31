# coding=utf-8
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
import config
from flask_login import LoginManager

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
# form = FlaskForm()
loginmanager=LoginManager()


# def initLoginManager(app):
#     login_manager = LoginManager(app)
#     login_manager.login_view = "login"
#     login_manager.login_message = u"未登录用户"
#     login_manager.login_message_category = "info"

def create_app(config_name):
    app = Flask(__name__, static_folder='static/assets')
    app.config.from_object(config)
    #config.SQLALCHEMY_DATABASE_URI.init_app(app)
    #app_cxt = app.app_context()
    #app_cxt.push()
    
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    loginmanager.init_app(app)
    # form.init_app(app)

    from  . main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    return app

