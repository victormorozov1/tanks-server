import pygame
from client.drawing.field import Field
from random import randrange as rd
from client.drawing.functions import *
from client.drawing.constants import *
from client.drawing.pictures import *


class CellField(Field):
    def __init__(self, szx, szy, field_arr, field_dict, cell_sz=CELL_SZ, bg=(255, 255, 255)):
        super().__init__(szx, szy, bg=bg)
        self.field_arr = field_arr
        self.field_dict = field_dict
        self.cell_sz = cell_sz
        self.n = szx // cell_sz
        self.m = szy // cell_sz
        self.szx = szx
        self.szy = szy
        self.bullets = []

    def draw_field(self, win, win_sz, start=(0, 0)):
        for i in range(max(0, start[1] // CELL_SZ), min(len(self.field_arr), start[1] // CELL_SZ + win_sz[1] // CELL_SZ + 2)):
            for j in range(max(0, start[0] // CELL_SZ), min(len(self.field_arr[i]), start[0] // CELL_SZ + win_sz[0] // CELL_SZ + 2)):
                x, y = j, i
                for pos in camera_coords(x * self.cell_sz, y * self.cell_sz, self.szx, self.szy, start):
                    if self.field_arr[i][j] != '.':
                        win.blit(self.field_dict[self.field_arr[i][j]], pos)

    def draw_objects(self, win, start=(0, 0)):
        try:
            for i in self.objects.values():
                i.draw(win, start=start)
        except BaseException as e:
            print(e)

    def show(self, win, win_sz, start=(0, 0)):
        win.fill(self.bg)
        self.draw_objects(win, start=start)
        self.draw_field(win, win_sz, start=start)
        for i in self.bullets:
            win.blit(bullet_pict, (i[0] - start[0], i[1] - start[1]))
        pygame.display.update()
