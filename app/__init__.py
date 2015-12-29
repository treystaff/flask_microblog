from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os
from flask.ext.login import LoginManager
from flask.ext.httpauth import HTTPBasicAuth

# Create the Flask application object
app = Flask(__name__)

# Tell the app to use the config setting defined in config.py
app.config.from_object('config')

# Initialize the database
db = SQLAlchemy(app)

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

auth = HTTPBasicAuth()

# Import is done after app creation to 'avoid circular import error'
from app import views, models
