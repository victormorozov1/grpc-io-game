from game_server.constants import *


class Object:
    def __init__(self, x, y, name, id=None):
        self.x = x
        self.y = y
        self.name = name
        self.id = id

    def __str__(self):
        return OBJECT_SEPARATOR.join([str(self.x), str(self.y), self.name])
