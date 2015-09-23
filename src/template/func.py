import flask
import hashlib
import logging
logger = logging.getLogger("app.func")

def redirect_login():
  return flask.redirect(flask.url_for('login'))

def get_gravatar_url(email):
  base_url = "https://www.gravatar.com/avatar/"
  email_hash = hashlib.md5(email.lower()).hexdigest()
  style = 'retro'
  full_url = "{}{}?d={}".format(\
    base_url, email_hash, style)
  return full_url
