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

    def connect(self):
        self.id = random_string(4)
        self._game_service.Connect(game_proto.PlayerInformation(id=self.id, szx=900, szy=900))
        self.connected = True
        print('connected')

    def get_map(self):
        s = self._game_service.GetMap(game_proto.Nothing()).s
        ret = []
        for i in s.split(SEPARATORS[0]):
            ret.append([])
            for j in i.split(SEPARATORS[1]):
                ret[-1].append(int(j))
                print(j, end=' ')
            print()
        return ret

    def _listen_for_players_movements(self):
        for message in self._game_service.GetPlayersMovements(game_proto.Id(s=self.id)):
            self._on_player_movement_received(message)

    def start_listening_for_players_movements(self, on_message_received):
        self._on_player_movement_received = on_message_received
        threading.Thread(target=self._listen_for_players_movements, daemon=True).start()

    def move(self):
        self._game_service.Move(game_proto.Id(s=self.id))

    def turn(self, direction):
        self._game_service.Turn(game_proto.TurnMessage(id=self.id, direction=direction))

    def fire(self):
        self._game_service.Fire(game_proto.Id(s=self.id))
