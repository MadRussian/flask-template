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
    
class DT_OBJ():
  """
  Create a datatables object on the server. The client side will used
  the result of get_dict to populate the datatables.
  """
  def __init__(self):
    self.cols = []
    self.cnum = {}
    self.rows = []
    self.obj = {}
    self.column_defs = []

  def set_cols(self, cols):
    self.cols = cols
    self.cnum = {}
    for idx, val in enumerate(self.cols):
      self.cnum.update({val[0]: idx})

  def set_column_defs(self, column_defs):
    self.column_defs = column_defs

  def add_row(self, row):
    self.rows.append(row)

  def set_row_cb(self, func):
    self.update('fnRowCallback', func)

  def update(self, key, val):
    self.obj.update({ key: val})

  def get_dict(self):
    self.update('aaData', self.rows)
    ao_cols = [ {"sTitle": idx[1]} for idx in self.cols ]

    self.update("aoColumns", ao_cols)
    self.update('cnum', self.cnum)
    self.update('aoColumnDefs', self.column_defs)
    return self.obj


