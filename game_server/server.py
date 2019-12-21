import grpc
from game_server.game_service import GameService
from game_server.grpc_out import game_pb2_grpc as game_grpc, game_pb2 as game_proto
from concurrent import futures


class Server:
    def __init__(self, port=5000, host='[::]', max_workers=10):
        self._port = port
        self._host = host
        self._server = grpc.server(futures.ThreadPoolExecutor(max_workers=max_workers))
        game_grpc.add_GameServicer_to_server(GameService(), self._server)

    def serve(self):
        print('Starting server...')
        self._server.add_insecure_port(str(self._host) + ':' + str(self._port))
        self._server.start()
        # print(f'Listening on {self._host}:{self._port}')
        print('Press CTRL+C to stop...')
        try:
            self._server.wait_for_termination()
        except KeyboardInterrupt:
            self._server.stop(None)
            print('Server is stopped')
