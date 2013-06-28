from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

from app import db
from app.twitter.forms import RegisterForm
from app.users.models import User
from app.twitter.models import Twitter 
from app.users.decorators import requires_login
import tweepy
from app.twitter import constants as CONSTANTS 

mod = Blueprint('twitter', __name__, url_prefix='/twitter')

@requires_login
@mod.route('/register/', methods=['GET', 'POST'])
def register():
  """
  Query from DB and create g.twitter 
  If we have token here we will have the 'api' and can do anything
  """
  g.twitter = None
  t = Twitter.query.filter_by(uid=g.user.id)
  if t.first():
    g.twitter = t.first()

  auth_url = ''
  api = None
  #Generate authen URL if User not add TwitterID or get access token if he already have
  if not g.twitter:
    auth = tweepy.OAuthHandler(CONSTANTS.CONSUMER_KEY, CONSTANTS.CONSUMER_SECRET, CONSTANTS.CALLBACK_URL)
    auth_url = auth.get_authorization_url()
    session['twitter_request_token']=(auth.request_token.key,auth.request_token.secret)
  else:
    atk = g.twitter.access_token_key
    ats = g.twitter.access_token_secret
    auth = tweepy.OAuthHandler(CONSTANTS.CONSUMER_KEY, CONSTANTS.CONSUMER_SECRET)
    auth.set_access_token(atk,ats)
    api = tweepy.API(auth_handler=auth)

  """
  Registration form 
  """
  form = RegisterForm(request.form)
  if form.validate_on_submit():
    twitter = Twitter(form.twitter_id.data, g.user.id)
    db.session.add(twitter)
    db.session.commit()

    flash('Thanks for adding twitter account')
    return redirect(url_for('users.home'))

  return render_template("twitter/register.html", form=form, twitter = t, oauth = auth_url, api = api)


@requires_login
@mod.route('/verify/', methods=['GET', 'POST'])
def verify():
  verifier= request.args['oauth_verifier']
  auth = tweepy.OAuthHandler(CONSTANTS.CONSUMER_KEY, CONSTANTS.CONSUMER_SECRET)
  token = session['twitter_request_token']
  del session['twitter_request_token']
  auth.set_request_token(token[0], token[1])

  try:
    auth.get_access_token(verifier)
  except tweepy.TweepError:
    print 'Error! Failed to get access token.'

  api = tweepy.API(auth)
  t = Twitter.query.filter_by(uid=g.user.id).first()
  if t:
    t.twitter_id = auth.get_username()
    t.access_token_key = auth.access_token.key 
    t.access_token_secret = auth.access_token.secret
  else:
    twitter = Twitter(auth.get_username(), g.user.id)
    twitter.access_token_key = auth.access_token.key 
    twitter.access_token_secret = auth.access_token.secret
    db.session.add(twitter)
  db.session.commit()
  return redirect(url_for('twitter.register'))

