import pygame, os
from client.game_client import *
from time import sleep
from client.pygame_field.game import Game
import pygame
from random import randrange as rd
from client.pygame_field.functions import *
from client.constants import *
from random import randrange as rd, choice


if __name__ == '__main__':
    gk = GameClient()
    x, y, direction = gk.connect()
    while not gk.connected:  # Вроде этот while можно убрать
        sleep(0.1)

    while True:
        if rd(40) < 37:
            gk.move()
        else:
            gk.turn(choice(['left', 'right', 'up', 'down']))
        sleep(0.03)
