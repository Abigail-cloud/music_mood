from app import db
from datetime import datetime

playlist_tracks = db.Table('playlist_tracks',
                           db.Column('playlist_id', db.Integer, db.ForeignKey('playlist.id')),
                           db.Column('track_id', db.Integer, db.ForeignKey('track.id'))
                           )


class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    mood = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    tracks = db.relationship('Track', secondary=playlist_tracks, backref=db.backref('playlists', lazy='dynamic'))


class Track(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    spotify_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(100))
    artist = db.Column(db.String(100))
