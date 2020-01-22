from game_server.files.constants import *


class Player:
    def __init__(self, tank, win_sz, id, name):
        self.tank = tank
        self.win_sz = win_sz
        self.is_moving = False
        self.id = id
        self.name = name

    def __str__(self):
        return str(self.id) + SEPARATORS[1] + str(self.tank.x) + SEPARATORS[1] + str(self.tank.y)
