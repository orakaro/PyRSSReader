from flask import Flask, flash, redirect, url_for, render_template, g, session
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from app.users.models import User
@app.before_request
def load_user():
  g.user = None
  if 'user_id' in session:
    g.user = User.query.get(session['user_id']);


@app.route('/')
def portal():
  flash('Welcome to vunhatminh.com')
  return redirect(url_for('users.login'))

from app.twitter.views import mod as twitterModule 
app.register_blueprint(twitterModule)

from app.facebook.views import mod as facebookModule 
app.register_blueprint(facebookModule)

from app.users.views import mod as usersModule
app.register_blueprint(usersModule)

from app.feed.views import mod as feedModule 
app.register_blueprint(feedModule)

# Later on you'll import the other blueprints the same way:
#from app.comments.views import mod as commentsModule
#from app.posts.views import mod as postsModule
#app.register_blueprint(commentsModule)
#app.register_blueprint(postsModule)
