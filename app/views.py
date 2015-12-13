from app import app

# The first view.
@app.route('/')
@app.route('/index')
def index():
    return "Hello_world!"

