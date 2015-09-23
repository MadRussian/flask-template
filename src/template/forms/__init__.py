from flask_wtf import Form
import wtforms
from wtforms import StringField, BooleanField, PasswordField, validators
from wtforms.validators import DataRequired, ValidationError, Required, EqualTo
import logging
logger = logging.getLogger("app.forms")

