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
        self.n = N
        self.m = N
        self.sleep = 0.01
        self.field = Field()
        self.names = dict()

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
        print(f'player {request.name} connected')
        x, y = self.field.free_cell()

        player_id, player_name = request.id, request.name

        client_win_size = request.szx, request.szy

        self.field.players[player_id] = Player(Tank(x, y, 100, 9, self.field, player_id[:2:]), client_win_size,
                                               player_id, player_name)
        self.names[player_id] = player_name
        self.names[player_id[:2:]] = player_name

        self.field.players[player_id].is_moving = True  # Заставляем игрока двинуться 1 раз чтобы его увидели другие

        return game_proto.Position(x=x, y=y, direction='up')

    def GetPlayersMovements(self, request, context):
        player_id = request.s
        self.field.player_movements_information[player_id] = []
        while context.is_active():
            arr = self.field.player_movements_information[player_id]
            self.field.player_movements_information[player_id] = []
            for i in arr:
                yield i
            sleep(self.sleep)

    def GetMap(self, request, context):
        return game_proto.Map(s=str(self.field.map))

    def Move(self, request, context):
        player = self.field.players[request.s]
        player.is_moving = True
        return game_proto.Nothing()

    def Turn(self, request, context):
        self.field.players[request.id].tank.moving_direction = request.direction

        for i in self.field.player_turns_information.keys():
            self.field.player_turns_information[i].append(game_proto.PlayerTurn(id=request.id[:2:], direction=request.direction))

        return game_proto.Nothing()

    def Fire(self, request, context):
        player_id = request.s
        try:
            self.field.players[player_id].tank.fire()
        except BaseException as e:
            print(e)
        return game_proto.Nothing()

    def GetAllBullets(self, request, context):
        while context.is_active():
            yield game_proto.Bullets(s=SEPARATORS[1].join([str(i) for i in self.field.bullets.values()]))
            sleep(self.sleep)

    def GetAllPlayers(self, request, context):
        print('in get all players')
        for i in self.field.players.values():
            try:
                yield game_proto.OtherPlayerInformation(id=i.id[:2:], x=i.tank.x, y=i.tank.y)
            except BaseException as e:
                print(e)
        print('end')

    def GetPlayersTurns(self, request, context):
        player_id = request.s
        self.field.player_turns_information[player_id] = []
        while context.is_active():
            arr = self.field.player_turns_information[player_id]
            self.field.player_turns_information[player_id] = []
            for i in arr:
                yield i
            sleep(self.sleep)

    def GetPlayerName(self, request, context):
        print('in get name')
        id = request.s
        print('id =', id)
        print(self.names.keys())
        try:
            return game_proto.Name(s=self.names[request.s])
        except BaseException as e:
            print('1', e)

    def GetPlayersHealthsChanging(self, request, context):
        player_id = request.s
        self.field.players_healths_changing_information[player_id] = []
        while context.is_active():
            arr = self.field.players_healths_changing_information[player_id]
            self.field.player_turns_information[player_id] = []
            for i in arr:
                yield i
            sleep(self.sleep)
