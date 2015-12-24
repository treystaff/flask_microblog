from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        flash('Login requested for OpenID={0}, remember_me={1}'.format(
            form.openid.data, str(form.remember_me.data)
        ))

        return redirect('/index')

    return render_template('login.html', title='Sign In', form=form,
                           providers=app.config['OPENID_PROVIDERS'])
