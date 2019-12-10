from client.game_client import GameClient
import pygame
from client.game.game import Game


class App(Game):
    def __init__(self):
        super().__init__(500, 500)
        self.client = GameClient()

    def on_message_recieved(self, message):
        print(message.x, message.y)
        print(message.field, end='\n\n\n')

        """self.field.remove_all_objects()
        for i in message.split(';'):
            x, y, obj = i.split('|')
            x, y = int(x), int(y)
            if obj == 'P':"""


    def start(self):
        self.client.start_listen_messages(self.on_message_recieved)
        self.run()



    def handle_event(self, ev):
        if ev.type == pygame.MOUSEBUTTONDOWN:
            pass
        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_LEFT:
                self.client.make_step(-10, 0)
            elif ev.key == pygame.K_RIGHT:
                self.client.make_step(10, 0)
            elif ev.type == pygame.K_UP:
                self.client.make_step(0, -10)
            elif ev.type == pygame.K_DOWN:
                self.client.make_step(0, 10)
