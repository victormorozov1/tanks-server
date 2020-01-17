from game_server.grpc_out import game_pb2 as game_proto, game_pb2_grpc as game_grpc
from time import sleep
from random import choice, randrange
from game_server.constants import *
from game_server.functions import *
from math import sqrt, floor, sin, pi
from game_server.map_generating import *
from game_server.map import *
from game_server.player import *
from game_server.classes.tanks import *
from game_server.field import *


class GameService(game_grpc.GameServicer):
    def __init__(self):
        self.map = Map(10, 10)
        self.n = N
        self.m = N
        self.sleep = 0.01
        self.field = Field()

    def game_iteration(self):
        for id in self.field.objects.keys():
            self.field.make_step(id)

    def Connect(self, request, context):
        print('New player connected!')

        x, y = self.field.free_cell()
        print('coords of new player', x, y)

        player_id = request.id
        print('new player id =', player_id)

        client_win_size = request.szx, request.szy
        print('client win size', client_win_size)

        self.field.objects[player_id] = Player(Tank(x, y, [], 100, 9), client_win_size)

        print('returning nothing')
        return game_proto.Nothing()

    def GetPlayersMovements(self, request, context):
        player_id = request.s
        print('player with id', player_id, 'want to get players movements')
        self.field.player_movements_information[player_id] = []
        while context.is_active():
            arr = self.field.player_movements_information[player_id]
            print('in GetPlayersMovements    arr =', arr)
            self.field.player_movements_information[player_id] = []
            for i in arr:
                print('returning id =', i.id, 'mave_x =', i.move_x, 'move_y =', i.move_y)
                yield i
                print('okkk')
            sleep(self.sleep)

    def GetMap(self, request, context):
        print('in get map')
        return game_proto.Map(s=str(self.map))

    def Move(self, request, context):
        print('Move id=', end='')
        print(request.s)
        player = self.field.objects[request.s]
        player.is_moving = True
        print('Move end')
        return game_proto.Nothing()
