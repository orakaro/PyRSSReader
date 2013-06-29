from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

from app import db
from app.feed.forms import RegisterForm
from app.rss_reader.parser import RSSParser
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

  form = RegisterForm(request.form)
  if form.validate_on_submit():
    insertFeed(form.link.data)
  g.feeds = createFeedList(g.user.id) 
  return render_template("feed/home.html", form=form, feeds=g.feeds)


def insertFeed(link):
  """
  Insert feed into DB 
  """
  rssParser = RSSParser(link)
  feed = Feed(rssParser.getName(), rssParser.getHref())
  db.session.add(feed)
  db.session.commit()
  justAdd = Feed.query.filter_by(link=link).first() 
  feeduser = FeedUser(justAdd.getId(), g.user.id)
  db.session.add(feeduser)
  db.session.commit()


def createFeedList(uid):
  """
  Query feeds from DB 
  Use RSSParser to get detail and show
  """
  rel = {} 
  fu_ary = FeedUser.query.filter_by(uid=uid).all()
  if fu_ary:
    for relation in fu_ary: 
      fl = Feed.query.filter_by(id=relation.fid).first()
      rel[fl.name] = createHeadline(fl.link)
  return rel

def createHeadline(link):
  """
  Use RSSParser to get detail 
  """
  rel={}
  rssParser = RSSParser(link)
  description = rssParser.getDescription()
  # Hacker News special link
  if link == "https://news.ycombinator.com/rss":
    description = rssParser.getDTO().entries[0].link
  rel["number"]=rssParser.getNumber()
  rel["href"]=rssParser.getHref()
  rel["head"]=rssParser.getHead()
  rel["description"]=description
  return rel

