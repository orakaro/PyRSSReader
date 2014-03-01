  from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

from app import db
fr  om app.facebook.forms import RegisterForm
from app.users.models import User
from app.facebook.models import Facebook
from app.users.decorators import requires_login
from app.facebook import constants as CONSTANTS
from flask_oauth import OAuth
from facepy import GraphAPI

mod = Blueprint('facebook', __name__, url_prefix='/facebook')
graph = None
oauth = OAuth()

facebook = oauth.remote_app('facebook',
    base_url='https://graph.facebook.com/',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    consumer_key=CONSTANTS.FACEBOOK_APP_KEY,
    consumer_secret=CONSTANTS.FACEBOOK_APP_SECRET,
    request_token_params={'scope': 'email'}
)


@requires_login
@mod.route('/register/', methods=['GET', 'POST'])
def register():
  """
  Query from DB and create g.facebook
  If we have token here we will have the 'graph God' and can do anything
  """
  g.facebook= None
  f = Facebook.query.filter_by(uid=g.user.id)
  if f.first():
    g.facebook= f.first()
  if g.facebook:
    graph = GraphAPI(g.facebook.access_token)
  else:
    graph = None
  """
  Registration form
  """
  form = RegisterForm(request.form)
  if form.validate_on_submit():
    facebook = Facebook(form.facebook_id.data, session['user_id'])
    db.session.add(facebook)
    db.session.commit()

    flash('Thanks for adding facebook account')
    return redirect(url_for('users.home'))

  return render_template("facebook/register.html", form=form, facebook = f, graph = graph)

@mod.route('/authen/')
def authen():
  return facebook.authorize(callback=url_for('facebook.facebook_authorized',
        next=request.args.get('next') or request.referrer or None,
        _external=True))

@mod.route('/register/authorized/')
@facebook.authorized_handler
def facebook_authorized(resp):
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    session['oauth_token'] = (resp['access_token'], '')
    f = Facebook.query.filter_by(uid=g.user.id).first()
    if f:
      f.facebook_id = facebook.get('/me').data['username']
      f.access_token = session['oauth_token'][0]
    else:
      f= Facebook(facebook.get('/me').data['username'], g.user.id)
      f.access_token = session['oauth_token'][0]
      db.session.add(f)
    db.session.commit()
    return redirect(url_for('facebook.register'))

@facebook.tokengetter
def get_facebook_oauth_token():
    return session.get('oauth_token')

