#!/bin/bash
# Setup an environment for working through this tutorial:
# http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

mkdir /code/flask_microblog
cd /code/flask_microblog

# This is required to get C extensions properly compiled for the following 
# python modules: flask-sqlalchemy, coverage (maybe others)
apt-get install python3-dev -y

# Install python-virtualenv. Note Python3 ships w/ venv, 
# but broken on ubuntu distributions. This is a workaround
apt-get install python-virtualenv -y
# Create the flask virtual env (use python3 for this project)
virtualenv flask -p python3

# Activate the flask venv
source flask/bin/activate

# Install dependencies required for this tutorial. 
pip install flask flask-login flask-openid flask-mail flask-sqlalchemy 
pip install sqlalchemy-migrate flask-wooshalchemy flask-wtf flask-babel
pip install guess_language flipflop coverage

# Now create the project directory structure. (remove if create a git)
cd ..
mkdir -p app/{static,templates}
mkdir tmp

