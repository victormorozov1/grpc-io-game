from client.game.object import Object
import pygame


class Field:
    def __init__(self, szx, szy, bg=(255, 255, 255)):
        self.szx = szx
        self.szy = szy
        self.last_id = 0
        self.objects = []
        self.bg = bg

    def remove_all_objects(self):
        self.objects = []

    def add_object(self, picture, x, y):
        self.last_id += 1
        self.objects.append(Object(self.last_id, picture, x, y))
        return self.last_id

    def get_object_by_id(self, id):
        for i in self.objects:
            if i.id == id:
                return i

    def remove_object(self, id):
        for i in range(len(self.objects)):
            if self.objects[i].id == id:
                del self.objects[i]
                break

    def move_object_to(self, id, x, y):
        obj = self.get_object_by_id(id)
        obj.x = x
        obj.y = y

    def move_object_on(self, id, dx, dy):
        obj = self.get_object_by_id(id)
        obj.x += dx
        obj.y += dy

    def show(self, win):
       # print('show', len(self.objects), 'objects')
        win.fill(self.bg)
        for i in self.objects:
            win.blit(i.picture, (i.x, i.y))
        pygame.display.update()
