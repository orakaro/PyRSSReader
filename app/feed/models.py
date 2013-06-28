from app import db

class Feed(db.Model):

    __tablename__ = 'feed'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    link = db.Column(db.String(200))

    def __init__(self, name=None, link=None):
      self.name = name 

    def getLink(self):
      return self.link

    def getName(self):
      return self.name

    def __repr__(self):
        return '<Feed %r>' % (self.name)


class FeedUser(db.Model):

    __tablename__ = 'feeduser'
    id = db.Column(db.Integer, primary_key=True)
    fid = db.Column(db.Integer, db.ForeignKey('feed.id'))
    uid = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, name=None, link=None):
      self.name = name 

    def getFeed(self):
      return self.fid

    def getUser(self):
      return self.uid

    def __repr__(self):
        return '<FeedUser %r>' % (self.id)


