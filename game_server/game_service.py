from game_server.grpc_out import game_pb2 as game_proto, game_pb2_grpc as game_grpc
from time import sleep
from random import choice, randrange
from game_server.object import Object
from game_server.constants import *
from game_server.functions import *


class GameService(game_grpc.GameServicer):
    def __init__(self):
        self.a = 1
        self.b = 1
        self.field = [Object(300, 200, 'R')]
        self.n = 10
        self.m = 10
        self.session = dict()
        self.sleep = 0.01

    def free(self, x, y, ignore=[]):
        for i in self.field:
            if i not in ignore:
                if abs(x - i.x) < CELL_SZ and abs(y - i.y) < CELL_SZ:
                    return False
        return True

    def free_cell(self):
        x, y = randrange(WIN_SZ_X - CELL_SZ), randrange(WIN_SZ_Y - CELL_SZ)
        while not self.free(x, y):
            x, y = randrange(WIN_SZ_X - CELL_SZ), randrange(WIN_SZ_Y - CELL_SZ)
        return x, y

    def field_str(self):
        ret = FIELD_SEPARATOR.join([str(i) for i in self.field])
        return ret

    def GetField(self, request, context):
        print('New player connected')

        x, y = self.free_cell()
        self.session[request.s] = Object(x, y, 'P')
        player = self.session[request.s]
        print('Coords of new player', x, y)

        self.field.append(player)

        while context.is_active():
            yield game_proto.GameInformation(x=player.x, y=player.y, field=self.field_str())
            sleep(self.sleep)

        self.field.remove(player)

    def _make_step(self, obj, move_x, move_y):  # Делает шаг по 1 пикселю
        print('making step on', move_x, move_y)
        obj.x += move_x
        obj.y += move_y
        if not self.free(obj.x, obj.y, ignore=[obj]):
            obj.x -= move_x
            obj.y -= move_y

    def MakeStep(self, request, context):
        print('making step')
        print('id =', request.id)
        obj = self.session[request.id]
        print('session get')
        for i in range(abs(request.move_x)):
            self._make_step(obj, abs(request.move_x) // request.move_x, 0)
        for i in range(abs(request.move_y)):
            self._make_step(obj, 0, abs(request.move_y) // request.move_y)
        return game_proto.Nothing()
