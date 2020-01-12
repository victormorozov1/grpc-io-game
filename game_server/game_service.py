from game_server.grpc_out import game_pb2 as game_proto, game_pb2_grpc as game_grpc
from time import sleep
from random import choice, randrange
from game_server.object import Object
from game_server.constants import *
from game_server.functions import *
from math import sqrt, floor, sin, pi


class GameService(game_grpc.GameServicer):
    def __init__(self):
        self.a = 1
        self.b = 1
        self.num_of_start_objects = 100
        self.get_start_field()
        self.n = 10
        self.m = 10
        self.session = dict()
        self.sleep = 0.01
        self.moving = dict()

    def game_iteration(self):
        for id in self.session.keys():
            self.make_step(id)

    def get_start_field(self):
        self.field = []
        for i in range(self.num_of_start_objects):
            self.field.append(Object(*self.free_cell(), 'R'))

    def free(self, x, y, ignore=[]):
        for i in self.field:
            if i not in ignore:
                if abs(x - i.x) < CELL_SZ and abs(y - i.y) < CELL_SZ:
                    return False
        return x in range(0, FIELD_SZ_X) and y in range(0, FIELD_SZ_Y)

    def free_cell(self):
        x, y = randrange(FIELD_SZ_X - CELL_SZ), randrange(FIELD_SZ_Y - CELL_SZ)
        while not self.free(x, y):
            x, y = randrange(FIELD_SZ_X - CELL_SZ), randrange(FIELD_SZ_Y - CELL_SZ)
        return x, y

    def field_str(self, client_win_size, player_id):
        player_pos = self.session[player_id].x, self.session[player_id].y
        lx, rx = player_pos[0] - client_win_size[0] // 2, player_pos[0] + client_win_size[0] // 2
        ly, ry = player_pos[1] - client_win_size[1] // 2, player_pos[1] + client_win_size[1] // 2
        ret = ''

        for i in self.field:
            if i.x in range(lx - CELL_SZ, rx + CELL_SZ) and i.y in range(ly - CELL_SZ, ry + CELL_SZ):
                if i.id == player_id:
                    i.name = 'Y'
                    ret += FIELD_SEPARATOR + str(i)
                    i.name = 'P'
                else:
                    ret += FIELD_SEPARATOR + str(i)

        return ret.strip(FIELD_SEPARATOR)

    def GetField(self, request, context):
        print('New player connected')

        x, y = self.free_cell()
        player_id = request.s
        print('coords of new player', x, y)
        client_win_size = request.szx, request.szy
        print('client win size', client_win_size)
        self.session[request.s] = Object(x, y, 'P', id=player_id)
        player = self.session[player_id]
        self.moving[player_id] = [0, 0]

        self.field.append(player)

        while context.is_active():
            yield game_proto.GameInformation(x=player.x, y=player.y, field=self.field_str(client_win_size, player_id))
            sleep(self.sleep)

        self.field.remove(player)

    def make_step_by_pixel(self, obj, move_x, move_y):  # Делает шаг по 1 пикселю
        obj.x += move_x
        obj.y += move_y
        if not self.free(obj.x, obj.y, ignore=[obj]):
            obj.x -= move_x
            obj.y -= move_y

    def get_move(self, player_id):
        player = self.session[player_id]
        x1, y1 = player.x, player.y
        x2, y2 = self.moving[player_id]
        dx, dy = abs(x2 - x1), abs(y2 - y1)

        if dx == 0:
            dx = 0.0000001
        k = dy / dx

        move_x = sqrt(MAX_SPEED ** 2 / (k ** 2 + 1)) * sign(x2 - x1)
        move_y = abs(move_x) * k * sign(y2 - y1)

        return int(move_x), int(move_y)

    def make_step(self, player_id):
        global move_x, move_y

        obj = self.session[player_id]
        move_x, move_y = self.get_move(player_id)

        for i in range(abs(move_x)):
            self.make_step_by_pixel(obj, abs(move_x) // move_x, 0)
        for i in range(abs(move_y)):
            self.make_step_by_pixel(obj, 0, abs(move_y) // move_y)

    def MakeStep(self, request, context):
        player = self.session[request.id]
        self.moving[request.id][0] = player.x + request.move_x
        self.moving[request.id][1] = player.y + request.move_y
        return game_proto.Nothing()
