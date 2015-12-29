from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm, auth
from .forms import LoginForm, RegisterForm
from .models import User


# The first view.
@app.route('/')
@app.route('/index')
@login_required
def index():
    # For demonstrative purposes, create a view that welcomes a
    #   logged in user.

    # Create an example user
    user = g.user

    # Create some fake posts
    posts = [
        {
            'author': {'username': 'Will'},
            'body': 'Portland is rainy'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The movie was so cool!'
        }
    ]

    # Render the index.html template in the app/static/ directory
    return render_template('index.html', title='Home', user=user, posts=posts)


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username=username).first()
    if not user or not user.verify_password(password):
        return False
    g.user = user
    return True


@app.before_request
def before_request():
    g.user = current_user


@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        if username is None or password is None:
            abort(400)  # Missing arguments

        if verify_password(username, password):
            login_user(g.user, remember=form.remember_me.data)
            flash('Logged in!')

            # Either returns user to page they navigated to before login,
            #   or sends them to the index page.
            return redirect(request.args.get('next') or url_for('index'))

    return render_template('login.html', title='Sign In', form=form)


@app.route('/register', methods=['GET','POST'])
def register():
    if g.user is not None and g.user.is_authenticated:
        # User is already logged in. No need to register.
        return redirect(url_for('index'))

    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        new_user = User(username=username, email=email)
        new_user.hash_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('New user "{0}" added!'.format(username))

        # The user has been created. Now redirect to login.
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/test', methods=['GET'])
@login_required
def test():
    return 'YAY'