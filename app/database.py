from sqlalchemy import create_engine,Column,String,Text,Integer,Time,Boolean
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import config
from flask_login import UserMixin

engine = create_engine(config.SQLALCHEMY_DATABASE_URI, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()
# Base.metadata.create_all(bind=engine)

def init_db():
	Base.metadata.create_all(bind=engine)
def drop_db():
    Base.metadata.drop_all(bind=engine)

class User(Base, UserMixin):
	__tablename__='users'
	is_active=True
	is_anonymous=False
	is_authenticated=False
	id=Column('id', Integer,primary_key=True)
	name=Column('name', String(64),unique=True)
	passwd=Column('passwd', String(64))
	enable=Column('enable', Integer)
	
	def __repr__(self):
		return '<User %r>' % self.name

	def get_id(self):
		return unicode(self.id)

class Task(Base,UserMixin):
	__tablename__='tasks'
	id=Column(Integer,primary_key=True)
	username=Column(String(64))
	title=Column(String(64))
	body=Column(Text)
	state=Column(String(64))

 	
 	def __repr__(self):
		return '<Task %r>' % self.title
	# def get_id(self):
	# 	return unicode(self.id)

init_db()

    
 