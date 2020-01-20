from game_server.files.constants import *


class Player:
    def __init__(self, tank, win_sz):
        self.tank = tank
        self.win_sz = win_sz
        self.is_moving = False

    def __str__(self):
        return str(self.tank.x) + SEPARATORS[1] + str(self.tank.y)
