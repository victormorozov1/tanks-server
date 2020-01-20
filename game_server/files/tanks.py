from game_server.files.constants import *
from game_server.files.bullets import *


class Tank:
    def __init__(self, x, y, healths, speed, field, id, moving_direction='up', szx=TANK_SZ, szy=TANK_SZ):
        self.x, self.y = x, y
        self.healths = healths
        # self.burrels = burrels
        # barrels - информация о всех дулах танка.
        self.speed = speed
        self.moving_direction = moving_direction
        self.field = field
        self.id = id
        self.num_fired_bullets = 0
        self.szx, self.szy = szx, szy

    def move(self, move_x, move_y):
        self.x += move_x
        self.y += move_y

    def fire(self):
        self.num_fired_bullets += 1
        global x, y
        if self.moving_direction == 'left':
            x = self.x - BULLET_INDENT
        elif self.moving_direction == 'up' or self.moving_direction == 'down':
            x = self.x + TANK_SZ // 2
        else:
            x = self.x + TANK_SZ + BULLET_INDENT

        if self.moving_direction == 'up':
            y = self.y - BULLET_INDENT
        elif self.moving_direction == 'left' or self.moving_direction == 'right':
            y = self.y + TANK_SZ // 2
        else:
            y = self.y + TANK_SZ + BULLET_INDENT

        self.field.bullets[self.id + str(self.num_fired_bullets)] = (
            Bullet(x, y, 2, 20, self.moving_direction, 100, self.field))
