from flask.helpers import url_for
from werkzeug.utils import redirect
from server import app, c

from flask import request, render_template, redirect, url_for


import chess


@app.route('/', methods =['POST', 'GET'])
def defult_route():
    if(request.method == 'POST'):
        return(f"{request.form['time']=},{request.form['message']=}")
    return render_template("post_html_test.html")

@app.route("/save", methods = ['POST','GET'])
def save_to_cache():
    if(request.method == 'POST'):
        c.set('test', 'worked')
        return redirect(url_for(load_cache))
    return render_template("cache_test.html")
@app.route("/load")
def load_cache():
    return str(c.get('test'))

@app.route("/board-test", methods = ['POST', 'GET'])
def test_board():
    if(request.method == 'POST'):
        board = chess.Board()
        board.push_san(request.form['move'])
        str_board = str(board)
        ls_board = [x for x in str_board]
        new_ls = [i for i in ls_board if i != "\n"]
        str_board = ''.join([i for i in new_ls if i != " "])
        return render_template("board_test.html", board = str_board)
    str_board = str(chess.Board())
    ls_board = [x for x in str_board]
    new_ls = [i for i in ls_board if i != "\n"]
    str_board = ''.join([i for i in new_ls if i != " "])
    return render_template("board_test.html", board = str_board)