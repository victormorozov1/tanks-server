from game_server.files.map import *
from game_server.files.constants import *
from random import randrange as rd
from game_server.grpc_out import game_pb2 as game_proto, game_pb2_grpc as game_grpc


class Field:
    def __init__(self):
        self.map = Map(N, N)
        self.players = dict()
        self.bullets = dict()
        self.player_movements_information = dict()

    def free(self, x, y, sz, ignore=[]):
        for id, i in self.players.items():
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
        # print('player_id in makepix', player_id)
        player = self.players[player_id]
        if self.free(player.tank.x + move_x, player.tank.y + move_y, TANK_SZ, ignore=[player]):
            player.tank.move(move_x, move_y)
            return move_x, move_y
        return 0, 0

    def get_move(self, player_id):
        player = self.players[player_id]

        if not player.is_moving:
            return 0, 0

        if player.tank.moving_direction == 'up':
            return 0, -MAX_SPEED
        elif player.tank.moving_direction == 'left':
            return -MAX_SPEED, 0
        elif player.tank.moving_direction == 'down':
            return 0, MAX_SPEED
        return MAX_SPEED, 0

    def make_step(self, player_id):
        # print('player with id =', player_id, 'is making step', end=' ')
        global move_x, move_y

        player = self.players[player_id]
        move_x, move_y = self.get_move(player_id)
        # print('on', move_x, move_y)
        if move_x == 0 and move_y == 0:
            return
        end_moving_x, end_moving_y = 0, 0

        for i in range(abs(move_x)):
            self.make_step_by_pixel(player_id, abs(move_x) // move_x, 0)

        for i in range(abs(move_y)):
            self.make_step_by_pixel(player_id, 0, abs(move_y) // move_y)

        for i in self.player_movements_information.keys():
            if i in self.player_movements_information:
                self.player_movements_information[i].append(
                    game_proto.PlayerMovement(id=player_id[:2:], new_x=player.tank.x, new_y=player.tank.y))

        self.players[player_id].is_moving = False

    def __str__(self):
        ret = ''
        for i in self.players.values():
            ret += SEPARATORS[0] + str(i)
        return ret
