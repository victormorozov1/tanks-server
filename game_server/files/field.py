from game_server.files.map import *
from game_server.files.constants import *
from random import randrange as rd
from game_server.grpc_out import game_pb2 as game_proto, game_pb2_grpc as game_grpc


class Field:
    def __init__(self):
        self.objects = dict()

        self.map = Map(N, N)

        self.player_movements_information = dict()
        self.player_turns_information = dict()
        self.players_healths_changing_information = dict()

    def free(self, x, y, sz, ignore=[]):
        for id, i in self.objects.items():
            if i not in ignore and id not in ignore:
                px, py = (x >= i.x and x - i.x <= sz or i.x >= x and i.x - x <= i.szx, y >= i.y and y - i.y <= sz or i.y >= y and i.y - y < i.szy)
                if px and py:
                    return False

        return self.map.area_is_free((x, y), sz, sz) and x in range(0, FIELD_SZ_X - sz) and y in range(0,
                                                                                                       FIELD_SZ_Y - sz)

    def free_cell(self):
        x, y = rd(FIELD_SZ_X), rd(FIELD_SZ_Y)
        while not self.free(x, y, TANK_SZ):
            x, y = rd(FIELD_SZ_X), rd(FIELD_SZ_Y)
        return x, y

    def add_object(self, obj):  # Обект может быть танком, снарядом или чем-то другим
        # единственные требования к добавляемому объекту - наличии полей x, y, szx, szy, id, move()
        self.objects[obj.id] = obj

    def __str__(self):
        ret = ''
        for i in self.objects.values():
            ret += SEPARATORS[0] + str(i)
        return ret
