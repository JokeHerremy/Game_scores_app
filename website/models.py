from . import db 
from sqlalchemy.sql import func

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game = db.Column(db.String(150))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    num_of_players = db.Column(db.Integer)
    scores = db.relationship('Score')

class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'))
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'))
    score = db.Column(db.Integer)

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    scores = db.relationship('Score')

