from client.game_client import *
from time import sleep


def print_movement(message):
    print('new movement: id=' + message.id, 'move_x=' + str(message.new_x), 'move_y=' + str(message.new_y))


def print_b_movement(message):
    print(message.s)


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

sleep(1)

#gk.start_listening_for_players_movements(print_movement)
gk.start_listening_for_bullets_positions(print_b_movement)


sleep(1)

print('fire')
gk.fire()

sleep(10)
