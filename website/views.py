from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
import requests 
import json
from .models import Game, Player, Score
from . import db


database = 'Game_Scores'
table = 'Games'

BASE = 'http://127.0.0.1:5000/'
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/enter_game', methods= ['GET', 'POST'])
def enter_game():
    if request.method == 'POST':
        data_game = request.form.get('game')
        data_date = request.form.get('date')
        
        data_num_of_players = request.form.get('num_of_players')
        new_game = Game(game=data_game, date=data_date, num_of_players=data_num_of_players)
        db.session.add(new_game)
        db.session.commit()
        flash('game saved', category='succes')
    return render_template("enter_game.html")

@views.route('/enter_player', methods= ['GET', 'POST'])
def enter_player():
    if request.method == 'POST':
        data = request.form.get('name')
        new_player = Player(name=data)
        db.session.add(new_player)
        db.session.commit()
        flash('New Player added', category='succes')
    return render_template('enter_player.html')    

@views.route('/player_entries', methods=['GET', 'DELETE'])
def player_entries():
    list = db.session.query(Player).all()
    return render_template('player_entries.html', players=list)

@views.route('/game_entries', methods= ['GET', 'DELETE'])
def game_entries():
    list = db.session.query(Game).all()
    return render_template("game_entries.html", games=list)

@views.route('/scoreboard')
def scoreboard():
    return render_template("scoreboard.html")


