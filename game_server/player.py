from game_server.constants import *


class Player:
    def __init__(self, tank, win_sz, moving_direction):
        self.tank = tank
        self.win_sz = win_sz
        self.moving_direction = moving_direction

    def __str__(self):
        return str(self.tank.x) + SEPARATORS[1] + str(self.tank.y)
