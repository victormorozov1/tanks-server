from client.game_client import *
from time import sleep
from random import randrange as rd, choice


if __name__ == '__main__':
    gk = GameClient()
    x, y, direction = gk.connect()
    while not gk.connected:  # Вроде этот while можно убрать
        sleep(0.1)

    while True:
        if rd(40) < 37:
            gk.move()
            sleep(0.1)
            if rd(10) == 5:
                gk.fire()
                print('fire')
        else:
            gk.turn(choice(['left', 'right', 'up', 'down']))
        sleep(0.03)