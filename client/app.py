from client.game_client import GameClient
import pygame
from client.game.game import Game
from client.constants import *
from client.functions import *


class App(Game):
    def __init__(self):
        super().__init__()
        self.client = GameClient()
        self.pictires = {'R': open_picture('rock.png'), 'P': open_picture('other_hero.png'), 'Y': open_picture('main_hero.png')}

    def on_message_recieved(self, message):
        global player_x, player_y
        self.field.remove_all_objects()
        arr = []

        for i in message.field.split(FIELD_SEPARATOR):
            arr.append(i.split(OBJECT_SEPARATOR))
            if arr[-1][2] == 'Y':
                player_x, player_y = int(arr[-1][0]), int(arr[-1][1])

        for i in arr:
            x, y, obj = i
            x, y = int(x) - player_x + self.szx // 2, int(y) - player_y + self.szy // 2
            self.field.add_object(self.pictires[obj], x, y)

    def start(self):
        self.client.start_listen_messages(self.on_message_recieved, self.szx, self.szy)
        self.run()

    def game_iteration(self):
        x, y = pygame.mouse.get_pos()
        self.client.make_step(x - self.szx // 2, y - self.szy // 2)
