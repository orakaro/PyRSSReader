from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

from app import db
from app.feed.forms import RegisterForm, DeleteForm
from app.rss_reader.parser import RSSParser
from app.users.models import User
from app.feed.models import Feed, FeedUser
from app.users.decorators import requires_login

mod = Blueprint('feed', __name__, url_prefix='/feed')

@requires_login
@mod.route('/detail/<feedName>', methods=['GET', 'POST'])
def detail(feedName = None):
  """
  Display the RSS Reader Detail 
  """
  link = request.args.get('feedLink',None)
  entriesAry = createEntriesAry(link) 

  form = RegisterForm(request.form)
  if form.validate_on_submit():
    insertFeed(form.link.data)
  return render_template("feed/detail.html", form=form, entriesAry=entriesAry)
 

@requires_login
@mod.route('/home/', methods=['GET', 'POST'])
def home():
  """
  Display the RSS Reader Home
  """

  rform = RegisterForm(request.form)
  dform = DeleteForm(request.form)

  # Unsubcribe a RSS link
  if dform.validate_on_submit():
    deleteFeed(dform.feedName.data)

  # Subcribe a RSS link
  if rform.validate_on_submit():
    insertFeed(rform.link.data)
  g.feeds = createFeedList(g.user.id) 

  return render_template("feed/home.html", rform = rform, dform = dform ,feeds = g.feeds)


def insertFeed(link):
  """
  Insert feed into DB 
  """
  rssParser = RSSParser(link)
  feed = Feed(rssParser.getName(), link)
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
  Use RSSParser to get HeadLine 
  """
  rel={}
  rssParser = RSSParser(link)
  # Save summary
  for entry in rssParser.getDTO().entries:
    f = open('app/templates/tmp/sum_'+entry.link[7:].replace('/','_'),'w')
    summary = entry.summary.encode('utf-8') 
    f.write(summary)
    f.close()

  rel["number"] = rssParser.getNumber()
  rel["href"] = rssParser.getHref()
  rel["head"] = rssParser.getHead()
  rel["entryLink"] = rssParser.getEntryLink()
  rel["link"] = link
  return rel

def createEntriesAry(link):
  """
  Use RSSParser to get detail 
  """
  rel = {}
  rssParser = RSSParser(link)
  rel = rssParser.getDTO().entries 
  # Write summary and content to sepetare file for later include
  for entry in rel:
    f = open('app/templates/tmp/'+entry.link[7:].replace('/','_'),'w')
    # Content or Description(summary)
    try:
      content = entry.content[0].value.encode('utf-8')
    except:
      content = entry.description.encode('utf-8') 
    f.write(content)
    f.close()
  return rel 

def deleteFeed(feedName):
  """
  Delete feed into DB 
  """
  # Find target feed but not delete, just delete relation between feed and user in feedUser
  targetFeed = Feed.query.filter_by(name = feedName).first() 
  deleteFeedUser = FeedUser.query.filter_by(fid = targetFeed.getId(), uid = g.user.id).first()
  db.session.delete(deleteFeedUser)
  db.session.commit()

