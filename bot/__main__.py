from client.game_client import *
from time import sleep
from random import randrange as rd, choice


if __name__ == '__main__':
    gk = []
    for i in range(10):
        gk.append(GameClient())
        sleep(1)

    for i in range(len(gk)):
        x, y, direction = gk[i].connect()
    i = 4
    while True:
        i += 1
        gk[i % len(gk)].move()
        sleep(0.1)
        for p in range(2):
            gk[(i + p) % len(gk)].fire()
        gk[(i * 2 % 77 - i // 6) % len(gk)].turn(choice(['left', 'right', 'up', 'down']))
        sleep(0.03)