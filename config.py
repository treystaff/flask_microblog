# Configuration file for Flask-WTF
import os

# Setup SQL Alchemy
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
# Disables flask-sqlalchemy's event-notification system (http://bit.ly/1YJ7WXl)
SQLALCHEMY_TRACK_MODIFICATIONS = False

WTF_CSRF_ENABLED = True  # Activates cross-site request forgery prevention
SECRET_KEY = 'you-will-never-guess'  # Needed when CSRF is enabled

OPENID_PROVIDERS = [
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}
    ]
