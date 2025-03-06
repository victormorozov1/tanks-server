from client.drawing.field import Field
import pygame
from time import sleep
from client.drawing.cell_field import CellField


class Game:
    def __init__(self, szx, szy, win, bg=(255, 255, 255), sleep=0.01, field='simple field', field_arr=None,
                 field_dict=None, cell_field_sz=64):
        if field == 'simple field':
            self.field = Field(szx, szy, bg=bg)
        elif field == 'cell field':
            self.field = CellField(szx, szy, field_arr, field_dict, cell_sz=cell_field_sz, bg=bg)
        else:
            self.field = field
            print('Warning: strange field', end=' ')
            try:
                print(field)
            except BaseException:
                print()
        self.sleep = sleep
        self.szx = szx
        self.szy = szy
        self.exit = False

    def handle_event(self, ev):
        pass

    def handle_events(self):
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                self.exit = True
            else:
                self.handle_event(i)

    def handle_pressed(self, key):
        pass

    def handle_all_pressed(self):
        keys = pygame.key.get_pressed()
        for i in range(len(keys)):
            if keys[i]:
                self.handle_pressed(i)

    def game_iteration(self):
        self.field.show(self.field.win)

    def run(self):
        self.running = True
        while self.running and not self.exit:
            self.handle_events()
            self.handle_all_pressed()
            self.game_iteration()

            sleep(self.sleep)
        return self.exit
