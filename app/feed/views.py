from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

from app import db
from app.feed.forms import RegisterForm
from app.users.models import User
from app.feed.models import Feed, FeedUser
from app.users.decorators import requires_login

mod = Blueprint('feed', __name__, url_prefix='/feed')

@requires_login
@mod.route('/home/', methods=['GET', 'POST'])
def home():
  """
  Display the RSS Reader Home
  """

  g.feeds = createFeedList(g.user.id) 

  return render_template("feed/home.html", feeds=g.feeds)



def createFeedList(uid):

  """
  Query from DB and create g.feeds
  """
  rel = {} 
  fu_ary = FeedUser.query.filter_by(uid=uid).all()
  if fu_ary:
    for relation in fu_ary: 
      fl = Feed.query.filter_by(id=relation.fid).first()
      rel[fl.name] = fl.link
  return rel

