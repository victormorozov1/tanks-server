from client.game_client import *


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


