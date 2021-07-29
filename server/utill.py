from server.common import games_cache
import pickle
from server.dataClasses import GameObject

def board_obj_to_formatted(board_obj) -> str:
    '''
    The job of this function take a chess.Board()
    instance get the repr then remove all spaces 
    and \ n thus rendering it formatted. 
    '''
    str_board = str(board_obj)
    ls_board = [x for x in str_board]
    new_ls = [i for i in ls_board if i != "\n"]
    str_board = ''.join([i for i in new_ls if i != " "])
    str_board = "abcdefgh" + str_board
    return str_board
    

def load_game(id) -> GameObject:
    pickled_game = games_cache.get(str(id))
    if(pickled_game == None):
        return GameObject(id)
    game = pickle.loads(pickled_game)
    return game

def save_game(id,game) -> None:
    pickled_game = pickle.dumps(game)
    games_cache.set(str(id),pickled_game)