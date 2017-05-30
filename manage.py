# coding=utf-8
import os
from app import create_app, db
from app.database import User, Task
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from app import config
# from flask.ext.login import LoginManager

#app = create_app(os.getenv())
app = create_app(config)
manager = Manager(app)
migrate = Migrate(app, db)

# app_cxt = app.app_context()
# app_cxt.push()

# def initLoginManager(app):
#     login_manager = LoginManager(app)
#     login_manager.login_view = "login"
#     login_manager.login_message = u"未登录用户"
#     login_manager.login_message_category = "info"


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()
