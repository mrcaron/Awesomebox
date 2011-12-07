from sqlalchemy import Column, String
from database import Base

class User(Base):
	__tablename__ = 'users'
	uid = Column(String(50), primary_key=True)
	mp3 = Column(String(150))

	def __init__(self, uid=None, mp3=None):
		self.uid = uid
		self.mp3 = mp3

	def __repr__(self):
		return '<User %r>' % (self.uid)
