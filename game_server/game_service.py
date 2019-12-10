from game_server.grpc_out import game_pb2 as game_proto, game_pb2_grpc as game_grpc
from time import sleep
from random import choice


class GameService(game_grpc.GameServicer):
    def __init__(self):
        self.a = 1
        self.b = 1
        self.field = [(22, 33, 'R'), (222, 333, 'R')]
        self.n = 10
        self.m = 10

    def free_cell(self):
        return 100, 300

    def field_str(self):
        ret = ';'.join(['|'.join([str(i) for i in j]) for j in self.field])
        print('String field returned', ret)
        return ret

    def Stream(self, request_iterator, context):
        print('New player connected')
        x, y = self.free_cell()
        print('New player coords:', x, y)
        self.field.append((x, y, 'P'))
        try:
            yield game_proto.ServerMessage(x=0, y=0, s='0')
            print('First answer returned')
        except BaseException as e:
            print('Error in sending first answer ' + str(e))
        for request in request_iterator:
            self.field[x][y] = '.'
            try:
                print('Command =', command)
                command = [int(i) for i in request.split(';')]
                x += command[0]
                y += command[1]
            except BaseException:
                print('Error in command')

            self.field[x][y] = 'P'
            yield game_proto.Field(x=x, y=y, field=self.field_str())
            sleep(0.1)

        print('Stream: end')
