from app import db

class Twitter(db.Model):

    __tablename__ = 'twitter'
    id = db.Column(db.Integer, primary_key=True)
    twitter_id= db.Column(db.String(50), unique=True)
    uid = db.Column(db.Integer, db.ForeignKey('user.id'))
    access_token_key = db.Column(db.String(200))
    access_token_secret = db.Column(db.String(200))

    def __init__(self, twitter_id=None, uid=None):
      self.twitter_id = twitter_id 
      self.uid = uid 

    def getTwitterID(self):
      return self.twitter_id

    def getUserID(self):
      return self.uid

    def __repr__(self):
        return '<Twitter %r>' % (self.twitter_id)
