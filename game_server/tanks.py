from game_server.constants import *
from game_server.bullets import *


class Tank:
    def __init__(self, x, y, healths, speed, field, moving_direction='up'):  # barrels - информация о всех дулах танка.
        self.x, self.y = x, y
        self.healths = healths
        # self.burrels = burrels
        self.speed = speed
        self.moving_direction = moving_direction
        self.field = field

    def move(self, move_x, move_y):
        self.x += move_x
        self.y += move_y

    def fire(self):
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

        self.field.bullets.append(Bullet(x, y, 2, 20, self.moving_direction))
