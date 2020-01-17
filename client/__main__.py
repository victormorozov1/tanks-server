from client.game_client import *
from time import sleep


def print_movement(message):
    print('new movement: id=' + message.id, 'move_x=' + str(message.move_x), 'move_y=' + str(message.move_y))


gk = GameClient()
gk.connect()
map = gk.get_map()
print()
for i in map:
    for j in i:
        if j == 0:
            print('.', end='')
        else:
            print('#', end='')
    print()

gk.start_listening_for_players_movements(print_movement)
sleep(1)
gk.turn('up')
sleep(1)
gk.move()

sleep(1)
gk.turn('down')
sleep(1)
gk.move()

sleep(1)
gk.turn('left')
sleep(1)
gk.move()

sleep(1)
gk.turn('right')
sleep(1)
gk.move()

sleep(10)
