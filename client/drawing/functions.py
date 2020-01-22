import pygame
from client.drawing.constants import *
from random import randrange as rd


def camera_coords(x, y, szx, szy, start):
    x -= start[0]
    y -= start[1]
    a = [0]
    ret = []
    for i in a:
        for j in a:
            ret.append((x + szx * i, y + szy * j))
    return ret


def sign(k):
    return abs(k) // k


def load_level(ind):
    ret = []
    f = open('data/levels/' + str(ind) + '.txt', 'r')
    for line in f:
        ret.append(line.strip('\n'))
    f.close()
    return ret


def load_picture(name, size=(CELL_SZ, CELL_SZ)):
    return pygame.transform.scale(pygame.image.load('client/drawing/data/' + name), size)




