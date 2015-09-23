#!/usr/bin/python

from __future__ import print_function
import os, sys
import argparse

def main():
  parser = argparse.ArgumentParser(description="Generate a flask template")
  parser.add_argument("project", help="project name")
  parser.add_argument('--port', default='5000',
                      help='Port to listen on. Default: 5000')
  args = parser.parse_args()
  project = args.project.replace(' ', '-')
  project_path = "build/{}".format(project)

  if not os.path.exists("build"):
    os.system("mkdir build")
  if os.path.exists(project_path):
    os.system("rm -rf {}".format(project_path))
  os.system("cp -R src {}".format(project_path))

  # Update the port
  os.system("sed -i 's/{{{{port}}}}/{}/' {}/{}".\
    format(args.port, project_path, 'runserver.py'))

  # Replace all instances of {{project}} with the project name
  file_arr = [
    'runserver.py',
    'template/config_sample.py',
    'template/__init__.py',
    'template/scripts/make_db.py',
    'template/db/__init__.py',
    'template/views/__init__.py',
    'template/views/main.py',
  ]
  for f_path in file_arr:
    os.system("sed -i 's/{{{{project}}}}/{}/' {}/{}".format(project, project_path, f_path))


  # Rename the directory to be the project name
  os.system("mv {}/template {}/{}".format(project_path, project_path, project))

  print("Project location: {}".format(project_path))
  print("---------------------")
  print("Go there and run [./runserver.py]")


if __name__ == "__main__":
  main()


