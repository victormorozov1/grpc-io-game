from game_server.constants import *


class Object:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name

    def __str__(self):
        return OBJECT_SEPARATOR.join([str(self.x), str(self.y), self.name])
