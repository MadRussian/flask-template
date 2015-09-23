from {{project}} import app, db, func
from functools import wraps
from flask import session, render_template, request, url_for, Blueprint, g
import flask
import logging
logger = logging.getLogger("app.views")

def is_logged_in(f):
  """Sample decorator to use in functions to verify a user is logged in"""
  @wraps(f)
  def decorated_function(*args, **kwargs):
    username = session.get('username')
    if username is None:
      return func.redirect_login()
    if db.user.User.get(username) is None:
      return func.redirect_login()
    return f(*args, **kwargs)
  return decorated_function

import main

# Import the blueprints
#from admin import bp_admin

# Register the blueprints
#app.register_blueprint(bp_admin, url_prefix='/admin')
