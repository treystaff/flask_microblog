# Contains SQLAlchemy database models
from app import db
from passlib.apps import custom_app_context as pwd_context


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    @property
    def is_authenticated(self):
        # Simply indicates a user can be authenticated.
        return True

    @property
    def is_active(self):
        # Active user. A situation where may want false is if user is banned
        return True

    @property
    def is_anonymous(self):
        # Fake users that should not loginto the system
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # Python 2
        except NameError:
            return str(self.id)  # Python 3

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def __repr__(self):
        return '<User {0}>'.format(self.nickname)


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)

    def __repr__(self):
        return '<Post {0}>'.format(self.body)