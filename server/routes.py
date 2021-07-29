from flask.helpers import url_for
from werkzeug.utils import redirect
from server import app

from server.common import cache, cache1

from flask import request, render_template, redirect, url_for

from server.utill import board_obj_to_formatted, load_game, save_game

import chess

import time


@app.route('/', methods =['POST', 'GET'])
def defult_route():
    if(request.method == 'POST'):
        return(f"{request.form['time']=},{request.form['message']=}")
    return render_template("post_html_test.html")

@app.route("/save", methods = ['POST','GET'])
def save_to_cache():
    if(request.method == 'POST'):
        cache.set('test', f'cache worked at {time.time()}')
        cache1.set('test', f'cache1 worked at {time.time()}')
        return redirect('/load')
    return render_template("cache_test.html")
@app.route("/load")
def load_cache():
    return f"<br>{cache.get('test')=}<br>{cache1.get('test')=}"

@app.route("/board-test", methods = ['POST', 'GET'])
def test_board():
    game = load_game(1)
    if(request.method == 'POST'):
        board = game.board
        board.push_san(request.form['move'])
        game.board = board
        str_board = board_obj_to_formatted(board)
        save_game(game.id,game)
        return render_template("board_test.html", board = str_board)
    str_board = board_obj_to_formatted(game.board)
    return render_template("board_test.html", board = str_board)