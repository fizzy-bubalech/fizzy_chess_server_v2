

def board_obj_to_formatted(board_obj) -> str:
    '''
    The job of this function take a chess.Board()
    instance get the repr then remove all spaces 
    and \ n thus rendering it formatted. 
    '''
    str_board = str(board_obj)
    ls_board = [x for x in str_board]
    new_ls = [i for i in ls_board if (i != "\n" or i != " ")]
    str_board = ''.join(new_ls)
    return str_board
    