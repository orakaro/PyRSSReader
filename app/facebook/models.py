from app import db

class Facebook(db.Model):

    __tablename__ = 'facebook'
    id = db.Column(db.Integer, primary_key=True)
    facebook_id= db.Column(db.String(50), unique=True)
    uid = db.Column(db.Integer, db.ForeignKey('user.id'))
    access_token= db.Column(db.String(200))

    def __init__(self, facebook_id=None, uid=None):
      self.facebook_id = facebook_id 
      self.uid = uid 

    def getFacebookID(self):
      return self.facebook_id

    def getUserID(self):
      return self.uid

    def __repr__(self):
        return '<Facebook %r>' % (self.facebook_id)
