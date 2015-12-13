from flask import Flask

# Create the Flask application object
app = Flask(__name__)

# Import is done after app creation to 'avoid circular import error'
from app import views