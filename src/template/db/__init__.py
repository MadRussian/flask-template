# Initial DB columns
# User, Groups, Roles, Projects, Audit, Preferences

from {{project}} import db

DEFAULT_CASCADE = "all, delete-orphan"

def commit(msg=""):
  try:
    db.session.commit()
    print "Committed: {}".format(msg)
    return True
  except:
    db.session.rollback()
    print "Failed to commit: {}".format(msg)
  return False

def add(obj, msg="", do_commit=True):
  db.session.add(obj)
  if do_commit:
    commit(msg)
    return
  if len(msg):
    print "Successfully added: {}".format(msg)

def delete(obj, msg="", do_commit=True):
  db.session.delete(obj)
  if do_commit:
    commit(msg)
  else:
    print "Successfully deleted: {}".format(msg)

# Example:
# from file_name import Class
