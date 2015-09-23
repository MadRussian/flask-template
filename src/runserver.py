#!/usr/bin/python

from __future__ import print_function
import os, sys
venv = 'venv/bin/activate_this.py'
os.environ['CONFIG_FILE'] = 'config_sample.py'

def check_prg(name, install_info=None):
  if os.system("which {} > /dev/null".format(name)) != 0:
    print("ERROR: [{}] not found".format(name))
    if install_info is not None:
      print(install_info)
    sys.exit(1)

check_prg("pip", "Usual package: [python-pip]")
check_prg("virtualenv", "To install: [sudo pip install virtualenv]")

new_setup = False
if not os.path.exists(venv):
  new_setup = True
  print("{} does not exist. Creating it now...".format(venv))
  os.system("virtualenv venv")

try:
  execfile(venv, dict(__file__=venv))
except Exception as err:
  exit("Failed to start virtualenv: {}".format(err))

if new_setup:
  try:
    os.system("pip install -r requirements.txt")
  except Exception as err:
    exit("Failed to install requirements.txt")

from {{project}} import app
print("\n\nServer is now running. Connect to port {{port}}")
app.run(host='0.0.0.0', port={{port}},  debug=True)
