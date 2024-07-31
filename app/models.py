from . import db

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist = db.Column(db.String(100), nullable=False)
    venue = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    stage = db.Column(db.String(50))

    def __repr__(self):
        return f"Booking('{self.artist}', '{self.venue}', '{self.date}', '{self.stage}')"
