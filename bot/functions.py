from random import randrange as rd
import pygame
from client.constants import *


def open_picture(way):
    way = 'pictures/' + way
    try:
        return pygame.image.load(way)
    except BaseException as e:
        return pygame.image.load('client/' + way)


def random_string(ln):
    ret = ''
    for i in range(ln):
        ret += chr(rd(33, 125))
    return ret


def load_picture(name):
    return pygame.transform.scale(pygame.image.load('client/data/' + name), (CELL_SZ, CELL_SZ))


if __name__ == '__main__':
    print(random_string(10))
