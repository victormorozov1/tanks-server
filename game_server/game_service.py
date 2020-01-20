from game_server.grpc_out import game_pb2 as game_proto, game_pb2_grpc as game_grpc
from time import sleep
from random import choice, randrange
from game_server.files.constants import *
from game_server.files.functions import *
from math import sqrt, floor, sin, pi
from game_server.files.map import *
from game_server.files.player import *
from game_server.files.tanks import *
from game_server.files.field import *


class GameService(game_grpc.GameServicer):
    def __init__(self):
        self.map = Map(10, 10)
        self.n = N
        self.m = N
        self.sleep = 0.01
        self.field = Field()

    def game_iteration(self):
        for id in self.field.players.keys():
            self.field.make_step(id)

        deleted_bullets_id = []
        for id, bullet in self.field.bullets.items():
            if bullet.deleted:
                deleted_bullets_id.append(id)
            else:
                bullet.move()
        for i in deleted_bullets_id:
            del self.field.bullets[i]

    def Connect(self, request, context):
        print('New player connected!')

        x, y = self.field.free_cell()
        print('coords of new player', x, y)

        player_id = request.id
        print('new player id =', player_id)

        client_win_size = request.szx, request.szy
        print('client win size', client_win_size)

        self.field.players[player_id] = Player(Tank(x, y, 100, 9, self.field, player_id[:2:]), client_win_size)

        print('returning nothing')
        return game_proto.Nothing()

    def GetPlayersMovements(self, request, context):
        player_id = request.s
        print('player with id', player_id, 'want to get players movements')
        self.field.player_movements_information[player_id] = []
        while context.is_active():
            arr = self.field.player_movements_information[player_id]
            self.field.player_movements_information[player_id] = []
            for i in arr:
                yield i
            sleep(self.sleep)

    def GetMap(self, request, context):
        print('in get map')
        return game_proto.Map(s=str(self.map))

    def Move(self, request, context):
        print('Move id=', end='')
        print(request.s)
        player = self.field.players[request.s]
        player.is_moving = True
        print('Move end')
        return game_proto.Nothing()

    def Turn(self, request, context):
        print('turning id=', request.id, 'direction =', request.direction)
        self.field.players[request.id].tank.moving_direction = request.direction
        return game_proto.Nothing()
    
    def Fire(self, request, context):
        print('Fire')
        player_id = request.s
        print('player_id =', player_id)
        try:
            self.field.players[player_id].tank.fire()
        except BaseException as e:
            print(e)
        return game_proto.Nothing()

    def GetAllBullets(self, request, context):
        print('player want\'s to get all bullets')
        while context.is_active():
            yield game_proto.Bullets(s=SEPARATORS[1].join([str(i) for i in self.field.bullets.values()]))
            sleep(self.sleep)
