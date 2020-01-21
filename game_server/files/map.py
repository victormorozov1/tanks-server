from random import randrange as rd
from game_server.files.constants import *


class Map:
    def __init__(self, n, m):
        self.n, self.m = n, m
        self.get_map()
        self.convert_map()

    def get_map(self):  # Генерация карту в понятном для пользователя формате
        self.map = []
        for i in range(self.n):
            self.map.append([])
            for j in range(self.m):
                if j in [0, self.m - 1] or i in [0, self.n - 1]:
                    self.map[-1].append('#')
                elif i % 2 == 0:
                    self.map[-1].append(['#', '.'][rd(9) // 6])
                else:
                    self.map[-1].append(['.', '.'][rd(7) // 6])

    def convert_map(self):
        self.converted_map = []
        for i in range(len(self.map)):
            self.converted_map.append([])
            for j in range(len(self.map[i])):
                self.converted_map[-1].append(WALLS[self.map[i][j]])

    def is_free(self, x, y):
        return self.map[y // CELL_SZ][x // CELL_SZ] == '.'

    def area_is_free(self, start_pos, szx, szy):
        x1, y1 = start_pos
        x2, y2 = x1 + szx - 1, y1 + szy - 1
        return self.is_free(x1, y1) and self.is_free(x2, y1) and self.is_free(x1, y2) and self.is_free(x2, y2)

    def __str__(self):
        return SEPARATORS[0].join([SEPARATORS[1].join([str(i) for i in j]) for j in self.converted_map])


if __name__ == '__main__':
    map = Map(10, 10)
    print(map)
