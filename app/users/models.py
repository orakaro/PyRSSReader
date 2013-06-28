from app import db
from app.users import constants as CONST 

class User(db.Model):

    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(20))
    gender = db.Column(db.String(10))
    role = db.Column(db.SmallInteger, default=CONST.USER)
    status = db.Column(db.SmallInteger, default=CONST.NEW)
    facebook = db.relationship('Facebook', backref='user', lazy='dynamic')
    twitter = db.relationship('Twitter', backref='user', lazy='dynamic')

    def __init__(self, name=None, email=None, password=None, gender=None):
      self.name = name
      self.email = email
      self.password = password
      self.gender = gender 

    def getStatus(self):
      return CONST.STATUS[self.status]

    def getRole(self):
      return CONST.ROLE[self.role]

    def __repr__(self):
        return '<User %r>' % (self.name)
