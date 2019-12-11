from game_server.grpc_out import game_pb2 as game_proto, game_pb2_grpc as game_grpc
from time import sleep
from random import choice


class GameService(game_grpc.GameServicer):
    def __init__(self):
        self.a = 1
        self.b = 1
        self.field = [('R', 22, 33), ('R', 222, 333)]
        self.n = 10
        self.m = 10
        self.session = dict()
        self.sleep = 0.1

    def free_cell(self):
        return 100, 300

    def field_str(self):
        ret = ''
        for i in range(len(self.field)):
            el = self.field[i]
            if el[0] == 'R':
                ret += str(el[1]) + '|' + str(el[2]) + '|' + 'R'
            elif el[0] == 'P':
                ret += str(self.session[el[1]]['x']) + '|' + str(self.session[el[1]]['y']) + '|' + 'P'
            if i != len(self.field) - 1:
                ret += ';'
        return ret

    def GetField(self, request, context):
        print('New player connected')

        x, y = self.free_cell()
        self.session[request.s] = dict()
        session = self.session[request.s]
        session['x'] = x
        session['y'] = y
        print('Coords of new player', x, y)

        self.field.append(('P', request.s))

        while context.is_active():
            yield game_proto.GameInformation(x=session['x'], y=session['y'], field=self.field_str())
            sleep(self.sleep)

    def MakeStep(self, request, context):
        print('making step')
        print('id =', request.id)
        session = self.session[request.id]
        print('session get')
        session['x'] += request.move_x
        session['y'] += request.move_y
        print('step maked, new coords', session['x'], session['y'])
        return game_proto.Nothing()
