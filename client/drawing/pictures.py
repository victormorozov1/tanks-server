from client.drawing.functions import load_picture
from client.drawing.constants import *

tank_pict = load_picture('main_hero_tank.png', size=(CELL_SZ, CELL_SZ))
bullet_pict = load_picture('bullet.png', size=(8, 8))
bush_pict = load_picture('bush.png', size=(CELL_SZ, CELL_SZ))
box_pict = load_picture('wall.png', size=(CELL_SZ, CELL_SZ))
river_pict = load_picture('river.png', size=(CELL_SZ, CELL_SZ))
savers = []
for i in range(1, SAVERS_NUM + 1):
    savers.append(load_picture('saver' + str(i) + '.jpg', (SZX, SZY)))

