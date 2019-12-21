from client.game.field import Field
import pygame
from time import sleep


class Game:
    def __init__(self, bg=(255, 255, 255), sleep=0.01):
        pygame.init()
        display_size = pygame.display.Info()
        szx, szy = display_size.current_w, display_size.current_h
        self.field = Field(szx, szy, bg=bg)
        self.sleep = sleep

    def handle_event_exit(self, ev):
        if ev.type == pygame.QUIT:
            self.running = False

    def handle_event(self, ev):
        pass

    def handle_events(self):
        for i in pygame.event.get():
            self.handle_event(i)
            self.handle_event_exit(i)

    def handle_pressed(self, key):
        pass

    def handle_all_pressed(self):
        keys = pygame.key.get_pressed()
        for i in range(len(keys)):
            if keys[i]:
                self.handle_pressed(i)

    def game_iteration(self):
        pass

    def run(self):
        win = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
        self.running = True
        while self.running:
            self.handle_events()
            self.handle_all_pressed()
            self.game_iteration()
            self.field.show(win)

            sleep(self.sleep)
