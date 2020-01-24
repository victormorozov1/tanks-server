from random import randrange as rd
from game_server.files.constants import *
from random import choice


class Map:
    def __init__(self, n, m):
        self.n, self.m = n, m
        self.load_level()

    def get_map(self):  # Генерация карту в понятном для пользователя формате
        self.map = []
        for i in range(self.n):
            self.map.append([])
            for j in range(self.m):
                if j in [0, self.m - 1] or i in [0, self.n - 1]:
                    self.map[-1].append('#')
                else:
                    self.map[-1].append('.')
                print(self.map[i][j], end='')
            print()
        self.n, self.m = len(self.map[0]), len(self.map)

    def load_level(self):
        self.map = []
        f = open('game_server/files/levels/1.txt', 'r')
        for line in f:
            self.map.append(line.strip('\n'))
        f.close()

    def is_free(self, x, y):
        return self.map[y // CELL_SZ][x // CELL_SZ] in ['.', '@']

    def is_free_for_bullet(self, x, y):
        return self.map[y // CELL_SZ][x // CELL_SZ] in ['.', '@', '*']

    def area_is_free(self, start_pos, szx, szy):
        x1, y1 = start_pos
        x2, y2 = x1 + szx - 1, y1 + szy - 1
        return self.is_free(x1, y1) and self.is_free(x2, y1) and self.is_free(x1, y2) and self.is_free(x2, y2)

    def __str__(self):
        return SEPARATORS[0].join([''.join([i for i in j]) for j in self.map])


if __name__ == '__main__':
    map = Map(30, 30)
    print(map)
