from random import randrange as rd
from game_server.constants import *


def get_map(n, m):  # Генерация карту в понятном для пользователя формате
    map = []
    for i in range(n):
        map.append([])
        for j in range(m):
            if j in [0, m - 1] or i in [0, n - 1]:
                map[-1].append('#')
            elif i % 2 == 0:
                map[-1].append(['#', '.'][rd(9) // 6])
            else:
                map[-1].append(['.', '#'][rd(7) // 6])
    return map





def get_converted_map():
    return convert_map(get_map(N, N))


if __name__ == '__main__':
    print(get_converted_map())
    for i in get_map(50, 50):
        for j in i:
            print(j, end='')
        print()
