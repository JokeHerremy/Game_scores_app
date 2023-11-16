from flask import Blueprint, render_template, request, flash, jsonify, url_for
from flask_login import login_required, current_user
import requests 
import json
from .models import Game, Player, Score
from . import db
from datetime import date


database = 'Game_Scores'
table = 'Games'

BASE = 'http://127.0.0.1:5000/'
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")



@views.route('/enter_player', methods= ['GET', 'POST'])
def enter_player():
    if request.method == 'POST':
        data = request.form.get('name')

        player = Player.query.filter_by(name=data).first()
        if player:
            flash('player already exists', category='error')
        else:
            new_player = Player(name=data)
            db.session.add(new_player)
            db.session.commit()
            flash('New Player added', category='succes')

    return render_template('enter_player.html')    

@views.route('/player_entries', methods=['GET', 'DELETE'])
def player_entries():
    list = db.session.query(Player).all()
    return render_template('player_entries.html', players=list)

@views.route('/delete-player', methods=['POST'])
def delete_player():  
    player = json.loads(request.data)
    playerId = player['playerId']
    player = Player.query.get(playerId)
    if player:
        db.session.delete(player)
        db.session.commit()
    return jsonify({})



@views.route('/enter_game', methods= ['GET', 'POST'])
def enter_game():
    if request.method == 'POST':
        data_game = request.form.get('game')
        data_date = request.form.get('date')
        date_list = data_date.split('-')
        data_date = date(int(date_list[0]), int(date_list[1]), int(date_list[2]))
        data_num_of_players = request.form.get('num_of_players')
        new_game = Game(game=data_game, date=data_date, num_of_players=data_num_of_players)
        db.session.add(new_game)
        db.session.commit()
        flash('game saved', category='succes')
    return render_template("enter_game.html")

@views.route('/game_entries', methods= ['GET', 'DELETE'])
def game_entries():
    list = db.session.query(Game).all()
    return render_template("game_entries.html", games=list)

@views.route('/delete-game', methods=['POST'])
def delete_game():  
    game = json.loads(request.data)
    gameId = game['gameId']
    game = Game.query.get(gameId)
    if game:
        db.session.delete(game)
        db.session.commit()
    return jsonify({})



@views.route('/scoreboard')
def scoreboard():
    return render_template("scoreboard.html")


