from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

from app import db
from app.users.models import User

def load_user():
  g.user = None
  if 'user_id' in session:
    g.user = User.query.get(session['user_id']);


