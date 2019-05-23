from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import md5

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    posts = db.relationship('Post', backref='author', lazy='dynamic'),
    about_me = db.Column(db.String(128))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email, 
        self.set_password(password) 

    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def avatar(self, size):
        digest=  md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?s={}'.format(digest, size)

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    body = db.Column(db.String(140), nullable=False)
    timestamp = db.Column(db.DateTime, index=True,  default=datetime.utcnow, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))