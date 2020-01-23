from client.drawing.object import Object
import pygame


class Field:
    def __init__(self, szx, szy, bg=(255, 255, 255)):
        self.szx = szx
        self.szy = szy
        self.last_id = 0
        self.bg = bg
        self.objects = dict()
        pygame.init()

    def remove_all_objects(self):
        self.objects = pygame.sprite.Group()

    def add_object(self, id, obj):
        self.objects[id] = obj
        return obj

    def get_object_by_id(self, id):
        for i in self.objects:
            if i.id == id:
                return i
        return False

    def remove_object(self, id):
        del self.objects[id]

    def move_object_to(self, id, x, y):
        obj = self.get_object_by_id(id)
        obj.rect.x = x
        obj.rect.y = y

    def move_object_on(self, id, dx, dy):
        obj = self.get_object_by_id(id)
        obj.rect.x += dx
        obj.rect.y += dy

    def show(self, win):
        win.fill(self.bg)
        self.objects.draw(self.win)
        pygame.display.update()
