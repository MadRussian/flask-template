"""
@author Nodar Nutsubidze
@description Flask Bootstrap Template
"""
import flask
from flask.ext.sqlalchemy import SQLAlchemy

class ReverseProxied(object):
    '''Wrap the application in this middleware and configure the 
    front-end server to add these headers, to let you quietly bind 
    this to a URL other than / and to an HTTP scheme that is 
    different than what is used locally.

    In nginx:
    location /myprefix {
        proxy_pass http://192.168.0.1:5001;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Scheme $scheme;
        proxy_set_header X-Script-Name /myprefix;
        }

    :param app: the WSGI application
    '''
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        script_name = environ.get('HTTP_X_SCRIPT_NAME', '')
        if script_name:
            environ['SCRIPT_NAME'] = script_name
            path_info = environ['PATH_INFO']
            if path_info.startswith(script_name):
                environ['PATH_INFO'] = path_info[len(script_name):]

        scheme = environ.get('HTTP_X_SCHEME', '')
        if scheme:
            environ['wsgi.url_scheme'] = scheme
        return self.app(environ, start_response)

app = flask.Flask(__name__)
app.wsgi_app = ReverseProxied(app.wsgi_app)
app.config.from_envvar('CONFIG_FILE')
app.secret_key = app.config['SECRET_KEY']
db = SQLAlchemy(app)

# Logging - Set a basic stream log handler which will go into the
# uwsgi log.
import logging, logging.config, logging.handlers
_pkg_modules = [
  "app.func",
  "app.views",
  "app.views.main",
  "app.forms",
]
default_log_settings = {
  'level': 'INFO'
}
log_config = {
  'version': 1,
  'formatters': {
    'default': {
      'format': '[%(asctime)s] %(levelname)-8s %(module)s - %(funcName)s - %(message)s',
    },
  },
  'handlers': {
    'file': {
      'class': 'logging.StreamHandler',
      'formatter': 'default',
    },
  },
  'loggers': {},
  'root': { 'handlers': ['file']},
}
for module in _pkg_modules:
  log_config['loggers'].setdefault(module, default_log_settings)
try:
  logging.config.dictConfig(log_config)
except Exception, err:
  print "Failed to set logging: {}".format(err)

import {{project}}.db
import {{project}}.views
