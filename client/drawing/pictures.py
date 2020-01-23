from client.drawing.functions import load_picture
from client.drawing.constants import *

tank_pict = load_picture('blue1.png')
bullet_pict = load_picture('bullet.png', size=(8, 8))
savers = []
for i in range(1, SAVERS_NUM + 1):
    savers.append(load_picture('saver' + str(i) + '.jpg', (SZX, SZY)))

