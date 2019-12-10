import grpc
import threading
from client.grpc_out import game_pb2_grpc as game_grpc
from client.grpc_out import game_pb2 as game_proto


class GameClient:
    def __init__(self, port=5000, host='127.0.0.1'):
        self._port = port
        self._host = host
        self._channel = grpc.insecure_channel(f'{self._host}:{self._port}')
        self._game_service = game_grpc.GameStub(self._channel)
        self.move_x = 0
        self.move_y = 0

    def start_listen_messages(self, message_received):
        print('starting listening for messages')
        self._on_message_receive = message_received
        threading.Thread(target=self._listen_for_messages, daemon=True).start()

    def _listen_for_messages(self):
        for message in self._game_service.Stream(game_proto.Command(s=str(self.move_y) + ';' + str(self.move_x))):
            self.move_x, self.move_y = 0, 0
            self._on_message_receive(message)

    def make_step(self, move_x, move_y):
        self.move_x = move_x
        self.move_y = move_y
