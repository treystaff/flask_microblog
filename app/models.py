# Contains SQLAlchemy database models
from app import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    posts = db.relationship('Posts', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {0}>'.format(self.nickname)


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)

    def __repr__(self):
        return '<Post {0}>'.format(self.body)