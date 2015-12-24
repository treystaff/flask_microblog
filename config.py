# Configuration file for Flask-WTF
WTF_CSRF_ENABLED = True  # Activates cross-site request forgery prevention
SECRET_KEY = 'you-will-never-guess'  # Needed when CSRF is enabled

OPENID_PROVIDERS = [
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}
    ]
