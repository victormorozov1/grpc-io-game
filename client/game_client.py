import grpc
import threading
from client.grpc_out import game_pb2_grpc as game_grpc
from client.grpc_out import game_pb2 as game_proto
from client.functions import *


class GameClient:
    def __init__(self, port=5000, host='127.0.0.1'):
        self._port = port
        self._host = host
        self._channel = grpc.insecure_channel(f'{self._host}:{self._port}')
        self._game_service = game_grpc.GameStub(self._channel)
        self.move_x = 0
        self.move_y = 0

    def start_listen_messages(self, message_received, szx, szy):
        print('starting listening for messages')
        self._on_message_receive = message_received
        self.szx = szx
        self.szy = szy
        threading.Thread(target=self._listen_for_messages, daemon=True).start()

    def _listen_for_messages(self):
        self.id = random_string(10)
        for message in self._game_service.GetField(game_proto.Id(s=self.id, szx=self.szx, szy=self.szy)):
            self._on_message_receive(message)

    def make_step(self, move_x, move_y):
        print('client: making step', move_x, move_y)
        self._game_service.MakeStep(game_proto.Step(id=self.id, move_x=move_x, move_y=move_y))
