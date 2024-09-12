from app import db, login_manager
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    spotify_id = db.Column(db.String(64), unique=True)
    access_token = db.Column(db.String(256))
    refresh_token = db.Column(db.String(256))
    moods = db.relationship('Mood', backref='user', lazy='dynamic')

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))