from {{project}} import app, db, func
from functools import wraps
from flask import session, render_template, request, url_for, Blueprint
import flask
import logging
logger = logging.getLogger("app.views")

"""
# Sample Decorators to use in your views

def is_logged_in(f):
  @wraps(f)
  def decorated_function(*args, **kwargs):
    username = session.get('username')
    if username is None:
      return func.redirect_login()
    if db.user.User.get(username) is None:
      return func.redirect_login()
    return f(*args, **kwargs)
  return decorated_function

def is_admin(f):
  @wraps(f)
  def decorated_function(*args, **kwargs):
    user = db.user.User.get(session['username'])
    if user is not None:
      if user.admin:
        return f(*args, **kwargs)
    return flask.redirect(flask.url_for('dashboard'))
  return decorated_function
"""

def get_page_data(page="", tab=None):
  obj = {
    'page': page,
  }
  if tab is not None:
    obj['tab'] = tab
  return obj

import main

"""
Use Blueprints for sub items.

Example:
from admin import admin
app.register_blueprint(admin, url_prefix='/admin')
"""
