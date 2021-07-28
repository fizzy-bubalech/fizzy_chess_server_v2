from dataClasses import dataclass
from chess import Board

@dataclass
class GameObject:
    id : int
    board : Board
    
    def __init__(self) -> None:
        board = Board()
