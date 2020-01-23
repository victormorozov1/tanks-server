import grpc
import threading
from client.grpc_out import game_pb2_grpc as game_grpc
from client.grpc_out import game_pb2 as game_proto
from client.functions import *
from client.constants import *


class GameClient:
    def __init__(self, port=5000, host='127.0.0.1'):
        self._port = port
        self._host = host
        self._channel = grpc.insecure_channel(str(self._host) + ':' + str(self._port))
        self._game_service = game_grpc.GameStub(self._channel)
        self.move_x = 0
        self.move_y = 0
        self.connected = False  # Не забыть проверить на подключение если будет ошибка

    def connect(self, name='Cucumber'):
        self.id = random_string(4)
        position = self._game_service.Connect(game_proto.PlayerInformation(id=self.id, szx=900, szy=900, name=name))
        self.connected = True
        print('connected')
        return position.x, position.y, position.direction

    def get_map(self):
        s = self._game_service.GetMap(game_proto.Nothing()).s
        ret = []
        for i in s.split(SEPARATORS[0]):
            ret.append(i)
        return ret

    def move(self):
        try:
            self._game_service.Move(game_proto.Id(s=self.id))
        except BaseException as e:
            print(e)

    def turn(self, direction):
        try:
            self._game_service.Turn(game_proto.TurnMessage(id=self.id, direction=direction))
        except BaseException as e:
            print(e)

    def fire(self):
        try:
            self._game_service.Fire(game_proto.Id(s=self.id))
        except BaseException as e:
            print(e)

    def start_listening_for_messages(self, on_message_received, it):
        threading.Thread(target=self._listen_for_messages, daemon=True, args=(on_message_received, it)).start()

    def _listen_for_messages(self, on_message_received, it):
        for message in it:
            on_message_received(message)

    def start_listening_for_bullets_positions(self, on_message_received):
        self.start_listening_for_messages(on_message_received,
                                          self._game_service.GetAllBullets(game_proto.Nothing()))

    def start_listening_for_players_movements(self, on_message_received):
        self.start_listening_for_messages(on_message_received,
                                          self._game_service.GetPlayersMovements(game_proto.Id(s=self.id)))

    def start_listening_for_players_turns(self, on_message_received):
        self.start_listening_for_messages(on_message_received,
                                          self._game_service.GetPlayersTurns(game_proto.Id(s=self.id)))

    def start_listening_for_healths_changing(self, on_message_received):
        self.start_listening_for_messages(on_message_received,
                                          self._game_service.GetPlayersHealthsChanging(game_proto.Id(s=self.id)))

    def get_all_players(self):
        ret = []
        print('ok')
        for i in self._game_service.GetAllPlayers(game_proto.Nothing()):
            print('in for')
            ret.append((i.id, i.x, i.y, i.healths))
            print('appended')
        return ret

    def get_player_name(self, id):
        try:
            print('in get player name')
            ret = self._game_service.GetPlayerName(game_proto.Id(s=id))
            print('ret rec')
            return ret.s
        except BaseException as e:
            print(e)




