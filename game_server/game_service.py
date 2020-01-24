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
import copy


class GameService(game_grpc.GameServicer):
    def __init__(self):
        self.n = N
        self.m = N
        self.sleep = 0.01
        self.field = Field()
        self.points = dict()

    def kill(self, killer_id, victim_id):
        try:
            print(f'{killer_id} killed {victim_id}')
            if killer_id in self.points.keys():
                self.points[killer_id] += 10
            else:
                self.points[killer_id] = 10
            elem = game_proto.KillInformation(killer_id=killer_id, victim_name=self.field.objects[victim_id].name,
                                              killer_points=self.points[killer_id])
            for i in self.field.kill_information.keys():
                self.field.kill_information[i].append(elem)
        except BaseException as e:
            print('Error in kill', e)

    def GetKills(self, request, context):
        print('in gtk')
        id = request.s
        self.field.kill_information[id] = []
        while context.is_active():
            arr = self.field.kill_information[id]
            self.field.kill_information[id] = []
            for i in arr:
                print('returning')
                yield i
            sleep(self.sleep)

    def game_iteration(self):
        try:
            try:
                deleted_objects_id = []
                arr = self.field.objects.values()
                for obj in arr:
                    obj.move()
                    if obj.healths <= 0:
                        deleted_objects_id.append(obj.id)
            except BaseException as e:
                print('!!!!!!!!!!!!!!!!!!', e)
            try:
                for i in deleted_objects_id:
                    obj = self.field.objects[i]
                    if obj.object_type == 'tank':
                        self.kill(obj.killer_id, i)
                    del self.field.objects[i]
            except BaseException as e:
                print('!!!!!!!', e)
        except BaseException as e:
            print('Error in game_iteration', e)

    def Connect(self, request, context):
        x, y = self.field.free_cell()

        password, player_name = request.id, request.name
        id = password[:2:]

        self.field.add_object(Tank(x, y, 100, 10, self.field, password, player_name))

        self.field.objects[id].is_moving = True  # Заставляем игрока двинуться 1 раз чтобы его увидели другие,
        #                                                 мне просто день делать под это отдельную функцию)

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
        try:
            return game_proto.Map(s=str(self.field.map))
        except BaseException as e:
            pass

    def Move(self, request, context):
        password, id = request.s, request.s[:2:]
        player = self.field.objects[id]
        if password == player.password:
            player.is_moving = True
        return game_proto.Nothing()

    def Turn(self, request, context):
        password, id, direction = request.id, request.id[:2:], request.direction
        player = self.field.objects[id]
        if password == player.password:
            player.direction = direction

            for i in self.field.player_turns_information.keys():
                self.field.player_turns_information[i].append(game_proto.PlayerTurn(id=id, direction=direction))

        return game_proto.Nothing()

    def Fire(self, request, context):
        try:
            password, id = request.s, request.s[:2:]
            player = self.field.objects[id]
            if password == player.password:
                player.fire()
        except BaseException as e:
            print('Error in Fire', e)
        return game_proto.Nothing()

    def GetAllBullets(self, request, context):
        while context.is_active():
            yield game_proto.Bullets(s=SEPARATORS[1].join(
                [str(i) for i in filter(lambda x: x.object_type == 'bullet', self.field.objects.values())]))
            sleep(self.sleep)

    def GetAllPlayers(self, request, context):
        for i in self.field.objects.values():
            if i.object_type == 'tank':
                try:
                    yield game_proto.OtherPlayerInformation(id=i.id[:2:], x=i.x, y=i.y, healths=i.healths)
                except BaseException as e:
                    print(e)

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
        id = request.s[:2:]
        return game_proto.Name(s=self.field.objects[id].name)

    def GetPlayersHealthsChanging(self, request, context):
        player_id = request.s
        self.field.players_healths_changing_information[player_id] = []
        while context.is_active():
            try:
                arr = self.field.players_healths_changing_information[player_id]
                for i in arr:
                    yield i
                self.field.players_healths_changing_information[player_id] = []
            except BaseException as e:
                pass
            sleep(self.sleep)
