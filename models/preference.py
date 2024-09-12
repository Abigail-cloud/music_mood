from app import db


class Preference(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True)
    favorite_genres = db.Column(db.String(200))
    energy_level = db.Column(db.Float)
    traceability = db.Column(db.Float)
