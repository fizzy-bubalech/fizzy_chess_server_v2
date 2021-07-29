from dataclasses import dataclass
from chess import Board
import enum 
import time

class COLOR(enum):
    WHITE = 1
    BLACK = 2



@dataclass
class ClockObject:

    start_time_second : float #time in seconds since epoch start 
    white_time_seconds : float
    black_time_seconds : float 

    increment_seconds : float

    black_clock_running : bool
    white_clock_running : bool

    last_turn_start_seconds : float


    turn : COLOR 

    def __init__(self, white_time_minutes, black_time_minutes,increment_seconds) -> None:
        self.turn = COLOR.WHITE
        self.white_clock_running = False
        self.black_clock_running = False
        self.white_time_seconds = float(white_time_minutes*60)
        self.black_time_seconds = float(black_time_minutes*60)

        self.increment_seconds = increment_seconds
        
    def start_clock(self):
        self.start_time_second = time.time()
        self.last_turn_start_seconds = self.start_time_second
        self.white_clock_running = True

    def pass_turn(self):
        if(self.turn == COLOR.WHITE):
            self.white_time_seconds -= (time.time()- self.last_turn_start_seconds)
            if(self.white_time_seconds > 0):
                self.white_time_seconds += float(self.increment_seconds)
                self.white_clock_running = False
                self.black_clock_running = True
                self.last_turn_start_seconds = time.time()
                return True
            else:
                self.white_clock_running = False
                return False
        if(self.turn == COLOR.black):
            self.black_time_seconds -= (time.time()- self.last_turn_start_seconds)
            if(self.black_time_seconds > 0):
                self.black_time_seconds += float(self.increment_seconds)
                self.black_clock_running = False
                self.white_clock_running = True
                self.last_turn_start_seconds = time.time()
                return True
            else:
                self.black_clock_running = False
                return False


    


@dataclass
class GameObject:
    id : int
    board : Board

    game_start : bool = False #Wether the game has started 
    black_game_start : bool = False #wether black is ready to start
    white_game_start : bool = False #wether white is ready to start 
    game_over : bool = False #wether the game has ended 

    game_clock : ClockObject 


    
    def __init__(self, id) -> None:
        self.id = id
        self.board = Board()
        self.game_clock = GameObject(white_time_minutes=3,black_time_minutes=3,increment_seconds=1)
