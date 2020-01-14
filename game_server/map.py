from random import randrange as rd
from game_server.constants import *


class Map:
    def __init__(self, n, m):
        self.n, self.m = n, m
        self.get_map()
        self.convert_map()

    def get_map(self, n, m):  # Генерация карту в понятном для пользователя формате
        self.map = []
        for i in range(n):
            self.map.append([])
            for j in range(m):
                if j in [0, m - 1] or i in [0, n - 1]:
                    self.map[-1].append('#')
                elif i % 2 == 0:
                    self.map[-1].append(['#', '.'][rd(9) // 6])
                else:
                    self.map[-1].append(['.', '#'][rd(7) // 6])

    def convert_map(self):
        self.converted_map = []
        for i in range(len(self.map)):
            self.converted_map.append([])
            for j in range(len(self.map[i])):
                self.converted_map[-1].append(WALLS[self.map[i][j]])

    def is_free(self, x, y):
        return self.map[x // CELL_SZ][y // CELL_SZ] == '.'

    def area_is_free(self, start_pos, szx, szy):
        x1, y1 = start_pos
        x2, y2 = x1 + szx - 1, y1 + szy - 1
        return self.is_free(x1, y1), self.is_free(x2, y1), self.is_free(x1, y2), self.is_free(x2, y2)