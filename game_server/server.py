import grpc
from game_server.game_service import GameService
from game_server.grpc_out import game_pb2_grpc as game_grpc, game_pb2 as game_proto
from concurrent import futures
from time import sleep


class Server:
    def __init__(self, port=5000, host='[::]', max_workers=10, sleep=0.01):
        self._port = port
        self._host = host
        self._server = grpc.server(futures.ThreadPoolExecutor(max_workers=max_workers))
        self.service = GameService()
        game_grpc.add_GameServicer_to_server(self.service, self._server)
        self.sleep = sleep

    def serve(self):
        print('Starting server...')
        self._server.add_insecure_port(str(self._host) + ':' + str(self._port))
        self._server.start()
        print('Press CTRL+C to stop...')
        try:
            while True:
                self.service.game_iteration()
                sleep(self.sleep)
        except KeyboardInterrupt:
            self._server.stop(None)
            print('Server is stopped')
