from game_server.map import *
from game_server.constants import *
from random import randrange as rd


class Field:
    def __init__(self):
        self.map = Map(N, N)
        self.objects = dict()
        self.players_movements = dict()

    def clier_players_movements(self):
        self.players_movements = dict()

    def free(self, x, y, sz, ignore=[]):
        for id, i in self.objects.items():
            if i not in ignore and id not in ignore:
                if abs(x - i.tank.x) < CELL_SZ and abs(y - i.tank.y) < sz:
                    return False
        return self.map.area_is_free((x, y), sz, sz) and x in range(0, FIELD_SZ_X - sz) and y in range(0,
                                                                                                       FIELD_SZ_Y - sz)

    def free_cell(self):
        x, y = rd(FIELD_SZ_X), rd(FIELD_SZ_Y)
        while not self.free(x, y, TANK_SZ):
            x, y = rd(FIELD_SZ_X), rd(FIELD_SZ_Y)
        return x, y

    def make_step_by_pixel(self, player_id, move_x, move_y):  # Делает шаг по 1 пикселю
        player = self.objects[player_id]
        if self.free(player.x + move_x, player.y + move_y, TANK_SZ, ignore=[player]):
            player.tank.move(move_x, move_y)
            if player_id in self.players_movements:
                self.players_movements[player_id][0] += move_x
                self.players_movements[player_id][1] += move_y

    def get_move(self, player_id):
        player = self.objects[player_id]

        if player.moving_direction == 'up':
            return 0, MAX_SPEED
        elif player.moving_direction == 'left':
            return -MAX_SPEED, 0
        elif player.moving_direction == 'down':
            return 0, MAX_SPEED
        return MAX_SPEED, 0

    def make_step(self, player_id):
        global move_x, move_y

        player = self.objects[player_id]
        move_x, move_y = self.get_move(player_id)

        for i in range(abs(move_x)):
            self.make_step_by_pixel(player, abs(move_x) // move_x, 0)
        for i in range(abs(move_y)):
            self.make_step_by_pixel(player, 0, abs(move_y) // move_y)

    def __str__(self):
        ret = ''
        for i in self.objects.values():
            ret += SEPARATORS[0] + str(i)
        return ret
