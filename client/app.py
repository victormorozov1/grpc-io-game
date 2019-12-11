from client.game_client import GameClient
import pygame
from client.game.game import Game
from client.constants import *


class App(Game):
    def __init__(self):
        super().__init__(500, 500)
        self.client = GameClient()
        self.pictires = {'R': pygame.image.load('pictures\\rock.png'), 'P': pygame.image.load('pictures\\other_hero.png')}

    def on_message_recieved(self, message):
        self.field.remove_all_objects()
        for i in message.field.split(';'):
            x, y, obj = i.split('|')
            x, y = int(x), int(y)
            self.field.add_object(self.pictires[obj], x, y)

    def start(self):
        self.client.start_listen_messages(self.on_message_recieved)
        self.run()

    def handle_pressed(self, key):
        if key == pygame.K_LEFT:
            self.client.make_step(-SPEED, 0)
        elif key == pygame.K_RIGHT:
            self.client.make_step(SPEED, 0)
        elif key == pygame.K_UP:
            self.client.make_step(0, -SPEED)
        elif key == pygame.K_DOWN:
            self.client.make_step(0, SPEED)
