from functools import wraps

from app.users.models import User
from flask import g, flash, redirect, url_for, request, session

def requires_login(f):
  @wraps(f)
  def decorated_function(*args, **kwargs):
    if g.user is None:
      flash(u'You need to be signed in for this page.')
      return redirect(url_for('users.login', next=request.path))
    return f(*args, **kwargs)
  return decorated_function
