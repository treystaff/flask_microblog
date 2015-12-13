from flask import render_template
from app import app

# The first view.
@app.route('/')
@app.route('/index')
def index():
    # For demonstrative purposes, create a view that welcomes a
    #   logged in user.

    # Create an example user
    user = {'nickname': 'Trey'}

    # Create some fake posts
    posts = [
        {
            'author': {'nickname': 'Will'},
            'body': 'Portland is rainy'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The movie was so cool!'
        }
    ]

    # Render the index.html template in the app/static/ directory
    return render_template('index.html', title='Home', user=user, posts=posts)

