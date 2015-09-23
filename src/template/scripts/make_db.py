#!/usr/bin/python
import os, sys
from {{project}} import app, db, task_db

def recreate_db():
  print 'recreating db'
  db.session.rollback()
  db.drop_all()
  db.create_all()
  db.session.commit()

if __name__ == '__main__':
  recreate_db()
